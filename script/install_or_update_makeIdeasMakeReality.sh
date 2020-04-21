#!/bin/bash

# PURPOSE
# Automate the process of installations and deployment of this django project. With this script, you
# don't have to worry about what software would be needed, what are the configuration files that are
# needed to be set, what are the information needed by the django app to work, and most importantly
# you don't have to worry about missing any step with the deployment of the app. All you need is a
# computer running GNU/Linux-Ubuntu (other distros might need tweaks with the way these scripts are
# written), an internet connection, a copy of this script (just this script alone is enough, not
# necessarily the whole project), and some snacks to eat while watching the beautiful logs scrolling
# through the screen, with you consciously thinking that you don't have to think about anything!

# USAGE
#     bash /absolute/path/from/literally/anywhere/to/script/install_or_update_makeIdeasMakeReality.sh
#     or
#     bash ../relative/path/from/literally/anywhere/to/script/install_or_update_makeIdeasMakeReality.sh

# NOTE
# For future extensions to this script (just this script, not including those called within this
# script), always keep in mind to never use the path of this script to reference the project, such as
# the command readlink. It has to be emphasized that this script is technically not part of this
# project! The idea is that this could be run as a standalone script or as part of an existing
# project. This is just written to install a project or update an existing project. An example
# scenario that would result to hard-to-find failures is:
# 1. You have a checkout of the whole makeIdeasMakeReality project in /home/user1/Documents/
# 2. This script is in /home/user1/Documents/makeIdeasMakeReality/script/install_or_update_makeIdeasMakeReality.sh
# 3. You decided to deploy another instance of the project in /home/user1/Downloads/ using this script
#    located in Documents/makeIdeasMakeReality/script/
# 4. During execution of script, you will be asked where to deploy a new instance, you responded
#    /home/user1/Downloads/
# 5. New checkout is cloned in /home/user1/Downloads/makeIdeasMakeReality
# 6. Now, you want to locate and update config/environmentVariables within this script
# 7. Here will be the start of the problem
# 8. If you located that file by simply getting the path to the currently running script (which is in
#    Documents/) and simply did a cd ../config, you are accessing Documents/makeIdeasMakeReality/config,
#    not Downloads/makeIdeasMakeReality/config, which is the actual copy for the new instance.
# This scipt works by changing directory to the target project, and then invoking the other scripts
# located in the target project. Thus from the perspective of the other scripts, it is safe to use
# their path to reference the project, since they are technically part of the project.

APP_NAME="makeIdeasMakeReality"

GIT="git"
GIT_LOC=$(command -v ${GIT})
GIT_REPO="https://github.com/nponcian/makeIdeasMakeReality.git"

PYTHON3="python3"
PYTHON3_LOC=$(command -v ${PYTHON3})
PYTHON3_PIP="python3-pip"
PYTHON3_VENV="python3-venv"
PIP="pip"
PIP3="pip3"
PIP3_LOC=$(command -v ${PIP3})
VENV="venv"
VENV_ACTIVATE="${VENV}/bin/activate"

POSTGRESQL="postgresql"
POSTGRESQL_CONTRIB="postgresql-contrib"
LIBPQ_DEV="libpq-dev"
PSQL="psql"
PSQL_LOC=$(command -v ${PSQL})

NGINX="nginx"
NGINX_LOC=$(command -v ${NGINX})

CONFIG="config"
SCRIPT="script"
PIP3_REQUIREMENTS="config/pip3Requirements.txt"
SCRIPT_ENVIRONMENT_VARIABLES_EXPORTER="script/environmentVariablesExporter.sh"
SCRIPT_ENVIRONMENT_VARIABLES_FILLER="script/environmentVariablesFiller.py"
SCRIPT_GUNICORN_NGINX_CONFIG_FILES_SETUP="script/gunicornNginxConfigFilesSetup.sh"
SCRIPT_GUNICORN_SERVICE_FILLER="script/gunicornServiceFiller.py"
SCRIPT_INSTALL_OR_UPDATE_MAKEIDEASMAKEREALITY="script/install_or_update_makeIdeasMakeReality.sh"

func_printConfigPaths()
{
    # This assumes you are in the root project directory
    echo "For your reference, here are some useful configuration paths of the current project:"
    echo "    $(pwd)"
    echo "    $(pwd)/${CONFIG}"
    echo "    $(pwd)/${SCRIPT}"
    echo -n "Press enter key to continue... "
    read TEMP
}

func_printAndExecuteCommand()
{
    echo "---> Command: ${@}"
    eval "${@}" # eval is used to be able to run commands such as redirecting to a file via "">"
}

func_aptInstall()
{
    if [[ -z "${1}" ]]; then
        func_printAndExecuteCommand "sudo apt install ${@:2}"
    else
        echo "${1} is already installed"
    fi
}

func_acceptInput()
{
    echo "${2}"
    echo -n "---> Input: "
    read ${1}
}

func_setupApt()
{
    func_acceptInput SHOULD_UPGRADE "Upgrade package manager? (advisable if using new machine) [y/n]"
    if [[ "${SHOULD_UPGRADE}" == "y" || "${SHOULD_UPGRADE}" == "Y" ]]; then
        func_printAndExecuteCommand "sudo apt update && sudo apt upgrade"
    else
        echo "Package manager not upgraded"
    fi
}

func_setupGit()
{
    # If ${GIT_LOC} is empty while ${GIT} isn't:
    #     If everything is enclosed in quotes "", it will be translated to:
    #         func_aptInstall "" value_of_git_here
    #         - still passing on 2 variables to func_aptInstall
    #     Else if no quotes:
    #         func_aptInstall value_of_git_here
    #         - only 1 variable is passed to func_aptInstall
    # This behavior can be easily seen with
    #     cd $A_NON_EXISTING_VARIABLE
    #         translates to <cd > which changes directory to home
    #     cd "$A_NON_EXISTING_VARIABLE"
    #         translates to <cd ""> which stays on current directory
    func_aptInstall "${GIT_LOC}" "${GIT}"

    func_acceptInput PROJECT_DIR "Enter target path to ${APP_NAME} (e.g. ../../Documents)"
    eval PROJECT_DIR="${PROJECT_DIR}" # Substitutes special character for home "~" to absolute path

    if [[ ! -z "${PROJECT_DIR}" ]]; then
        func_printAndExecuteCommand "cd ${PROJECT_DIR}"
    fi

    if [[ ! -d "${APP_NAME}" ]]; then
        func_printAndExecuteCommand "git clone ${GIT_REPO}"
        func_printAndExecuteCommand "cd ${APP_NAME}"
    else
        func_printAndExecuteCommand "cd ${APP_NAME}"
        func_printAndExecuteCommand "git pull origin master"
    fi
}

func_setupPython()
{
    func_aptInstall "${PYTHON3_LOC}" "${PYTHON3}"
    func_aptInstall "${PIP3_LOC}" "${PYTHON3_PIP}" "${PYTHON3_VENV}"

    if [[ ! -d "${VENV}" ]]; then
        func_printAndExecuteCommand "${PYTHON3} -m ${VENV} ${VENV}"
    fi

    func_printAndExecuteCommand "source ${VENV_ACTIVATE}"
    func_printAndExecuteCommand "${PYTHON3} -m ${PIP} install -r ${PIP3_REQUIREMENTS}"
}

func_setupPostgreSql()
{
    func_aptInstall "${PSQL_LOC}" "${POSTGRESQL} ${POSTGRESQL_CONTRIB} ${LIBPQ_DEV}"
}

func_setupNginx()
{
    func_aptInstall "${NGINX_LOC}" "${NGINX}"
}

func_setupScripts()
{
    func_printAndExecuteCommand "chmod u+x\
        ${SCRIPT_ENVIRONMENT_VARIABLES_FILLER}\
        ${SCRIPT_GUNICORN_NGINX_CONFIG_FILES_SETUP}\
        ${SCRIPT_GUNICORN_SERVICE_FILLER}\
        ${SCRIPT_INSTALL_OR_UPDATE_MAKEIDEASMAKEREALITY}"

    func_printConfigPaths

    func_printAndExecuteCommand "./${SCRIPT_ENVIRONMENT_VARIABLES_FILLER}"
    func_printAndExecuteCommand "./${SCRIPT_GUNICORN_SERVICE_FILLER}"
    func_printAndExecuteCommand "./${SCRIPT_GUNICORN_NGINX_CONFIG_FILES_SETUP}"
}

func_additionalNotes()
{
    echo
    echo "================"
    echo "ADDITIONAL NOTES"
    echo "================"
    echo
    echo "PostgreSQL and its necessary dependencies that would be used to run with the project are"
    echo "already installed. The django settings to connect to the database are already functional."
    echo "But it should be noted that this script hasn't touched any database, and there are no"
    echo "plans to touch it in anyway due to its delicate nature. Thus, it is required to setup"
    echo "PostgreSQL roles and the database to be used for the project separately. The details"
    echo "should be the same with those configured in the environmentVariables file that was used"
    echo "to configure this project."
    echo
    echo "For local development and deployment where you would not use Gunicorn as the WSGI server,"
    echo "lets say you would be using the default Django provided WSGI server (the one used when you"
    echo "use <python3 manage.py runserver>), then you have to set environment variables for the"
    echo "configurations in settings.py by invoking:"
    echo "    source `readlink -f ${SCRIPT_ENVIRONMENT_VARIABLES_EXPORTER}`"
    # or # echo "    source $(readlink -f ${SCRIPT_ENVIRONMENT_VARIABLES_EXPORTER})"
    echo "Activate the created virtual environment:"
    echo "    source ${VENV_ACTIVATE}"
}

func_setupApt
func_setupGit # this changes directory to the location of the target makeIdeasMakeReality repository
func_setupPython
func_setupPostgreSql
func_setupNginx
func_setupScripts

func_additionalNotes

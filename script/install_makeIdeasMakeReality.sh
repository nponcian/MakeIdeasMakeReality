#!/bin/bash

APP_NAME="makeIdeasMakeReality"

GIT="git"
GIT_LOC=$(command -v ${GIT})
GIT_REPO="https://github.com/nponcian/makeIdeasMakeReality.git"

PYTHON3="python3"
PYTHON3_LOC=$(command -v ${PYTHON3})
PYTHON3_PIP="python3-pip"
PYTHON3_VENV="python3-venv"
PIP3="pip3"
PIP3_LOC=$(command -v ${PIP3})

func_printAndExecuteCommand()
{
    echo "---> Command: ${@}"
    ${@}
}

func_install()
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

func_upgradeApt()
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
    #         func_install "" value_of_git_here
    #         - still passing on 2 variables to func_install
    #     Else if no quotes:
    #         func_install value_of_git_here
    #         - only 1 variable is passed to func_install
    func_install "${GIT_LOC}" "${GIT}"

    func_acceptInput PROJECT_DIR "Enter target path to ${APP_NAME} (e.g. ../../Documents)"
    eval PROJECT_DIR="${PROJECT_DIR}" # Substitutes special character for home "~" to absolute path

    func_printAndExecuteCommand "cd ${PROJECT_DIR}"

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
    func_install "${PYTHON3_LOC}" "${PYTHON3}"
    func_install "${PIP3_LOC}" "${PYTHON3_PIP}" "${PYTHON3_VENV}"
}

func_upgradeApt
func_setupGit
func_setupPython

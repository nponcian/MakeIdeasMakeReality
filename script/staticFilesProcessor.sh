#!/bin/bash

# PURPOSE
# Setup the directory to where the static files would be stored

# USAGE
#     sudo bash /absolute/path/from/literally/anywhere/to/script/staticFilesProcessor.sh
#     or
#     sudo bash ../relative/path/from/literally/anywhere/to/script/staticFilesProcessor.sh
# Use sudo if the target location of the static files is not writable to the current user, such as
# if it is outside of the /home/user/... directory.

PROJECT_PATH=$(readlink -f "${BASH_SOURCE}" | xargs dirname | xargs dirname)
VENV="venv"
VENV_ACTIVATE="${PROJECT_PATH}/${VENV}/bin/activate"
SCRIPT="script"
SCRIPT_ENVIRONMENT_VARIABLES_EXPORTER="${PROJECT_PATH}/${SCRIPT}/environmentVariablesExporter.sh"

printAndExecuteCommand()
{
    echo "---> Command: ${@}"
    eval "${@}"
}

printAndExecuteCommand "source ${VENV_ACTIVATE}"
printAndExecuteCommand "source ${SCRIPT_ENVIRONMENT_VARIABLES_EXPORTER}"
# printAndExecuteCommand "mkdir -v  -p ${MIMR_SETTINGS_STATIC_ROOT}" # not needed, automatically done
printAndExecuteCommand "${PROJECT_PATH}/manage.py collectstatic"

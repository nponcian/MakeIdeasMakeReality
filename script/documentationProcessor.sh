#!/bin/bash

# PURPOSE
# Setup the static html files from Sphinx documentation

# USAGE
#     bash /absolute/path/from/literally/anywhere/to/script/documentationProcessor.sh
#     or
#     bash ../relative/path/from/literally/anywhere/to/script/documentationProcessor.sh

PROJECT_PATH=$(readlink -f "${BASH_SOURCE}" | xargs dirname | xargs dirname)
VENV_ACTIVATE="${PROJECT_PATH}/venv/bin/activate"
SCRIPT_ENVIRONMENT_VARIABLES_EXPORTER="${PROJECT_PATH}/script/environmentVariablesExporter.sh"
DOCS="${PROJECT_PATH}/docs"
BUILD="${DOCS}/build"

printAndExecuteCommand()
{
    echo "---> Command: ${@}"
    eval "${@}"
}

printAndExecuteCommand "cd ${PROJECT_PATH}"

printAndExecuteCommand "source ${VENV_ACTIVATE}"
printAndExecuteCommand "source ${SCRIPT_ENVIRONMENT_VARIABLES_EXPORTER}"

printAndExecuteCommand "cd ${DOCS} && rm -rf ${BUILD}/*"
printAndExecuteCommand "make html"

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
HTML="${BUILD}/html"

printAndExecuteCommand()
{
    echo "---> Command: ${@}"
    eval "${@}"
}

func_acceptInput()
{
    echo "${2}"
    echo -n "---> Input: "
    read ${1}
}

printAndExecuteCommand "cd ${PROJECT_PATH}"

printAndExecuteCommand "source ${VENV_ACTIVATE}"
printAndExecuteCommand "source ${SCRIPT_ENVIRONMENT_VARIABLES_EXPORTER}"

printAndExecuteCommand "cd ${DOCS}"

if [[ -d "${HTML}" ]]; then
    func_acceptInput SHOULD_REBUILD "Force rebuilding of documentation? [y/n]"
    if [[ "${SHOULD_REBUILD}" == "y" || "${SHOULD_REBUILD}" == "Y" ]]; then
        printAndExecuteCommand "rm -rf ${BUILD}/*"
    fi
fi

printAndExecuteCommand "make html"

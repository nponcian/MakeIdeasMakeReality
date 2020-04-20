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
    echo "${@}"
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
    echo -n "Input: "
    read ${1}
}

func_setupGit()
{
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

func_setupGit
func_setupPython

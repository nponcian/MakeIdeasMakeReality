#!/bin/bash

APP_NAME="makeIdeasMakeReality"

GIT="git"
GIT_APP=$(command -v ${GIT})
GIT_APP_REPO="https://github.com/nponcian/makeIdeasMakeReality.git"

func_printAndExecuteCommand()
{
    echo ${1}
    ${1}
}

func_install()
{
    if [[ -z ${2} ]]; then
        func_printAndExecuteCommand "sudo apt install ${1}"
    fi
}

func_acceptInput()
{
    echo ${2}
    echo -n "Input: "
    read ${1}
}

func_install ${GIT} ${GIT_APP}

func_acceptInput PROJECT_DIR "Enter target path to ${APP_NAME} (e.g. ../../Documents)"
eval PROJECT_DIR=${PROJECT_DIR} # Substitutes home special character "~" to absolute path

func_printAndExecuteCommand "cd ${PROJECT_DIR}"

if [[ ! -d ${APP_NAME} ]]; then
    func_printAndExecuteCommand "git clone ${GIT_APP_REPO}"
    func_printAndExecuteCommand "cd ${APP_NAME}"
else
    func_printAndExecuteCommand "cd ${APP_NAME}"
    func_printAndExecuteCommand "git pull origin master"
fi

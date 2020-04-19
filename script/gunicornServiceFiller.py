#!/usr/bin/env python3

import fileinput

ENVIRONMENT_VARIABLES_FILE = "config/environmentVariables"
ENVIRONMENT_VARIABLES_PREFIX = "MIMR"
ENVIRONMENT_VARIABLES_SEP = "="

GUNICORN_SERVICE_FILE = "config/gunicorn.service"
GUNICORN_SERVICE_LINES_TO_IGNORE = ["ExecStart"]

def shouldIgnoreLine(line):
    if ENVIRONMENT_VARIABLES_PREFIX not in line: return True

    for toIgnore in GUNICORN_SERVICE_LINES_TO_IGNORE:
        if toIgnore in line: return True

    return False

envVariablesDict = dict()

with open(ENVIRONMENT_VARIABLES_FILE) as envVariablesFile:
    for line in envVariablesFile.readlines():
        line = line.strip()
        key, _, value = line.partition(ENVIRONMENT_VARIABLES_SEP)
        envVariablesDict[key] = value

for line in fileinput.input(GUNICORN_SERVICE_FILE, inplace = True):
    if shouldIgnoreLine(line):
        print(line, end = "")
    else:
        for key, value in envVariablesDict.items():
            line = line.replace(key, value)
        print(line, end = "")

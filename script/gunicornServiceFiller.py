#!/usr/bin/env python3

# PURPOSE
# Fill-up the config/gunicorn.service with the missing values from the available variables set within
# the file config/environmentVariables.

# USAGE
#     cd /path/to/makeIdeasMakeReality/
#     python3 script/gunicornServiceFiller.py

import fileinput

ENVIRONMENT_VARIABLES_FILE = "config/environmentVariables"
GUNICORN_VARIABLE_PREFIX = "MIMR_GUNICORN_"
GUNICORN_VARIABLE_SEP = "="

GUNICORN_SERVICE_FILE = "config/gunicorn.service"

NEW_LINE = "\n"
TAB = "    "

def isGunicornVariable(line):
    return line.strip().startswith(GUNICORN_VARIABLE_PREFIX)

def getGunicornVariablesDict():
    envVariablesDict = dict()
    with open(ENVIRONMENT_VARIABLES_FILE) as envVariablesFile:
        for line in envVariablesFile.readlines():
            line = line.strip()
            if not isGunicornVariable(line): continue
            key, _, value = line.partition(GUNICORN_VARIABLE_SEP)
            key = key[len(GUNICORN_VARIABLE_PREFIX):].casefold()
            envVariablesDict[key] = value
    return envVariablesDict

def updateGunicornFromEnvVariables(envVariablesDict):
    changedPairs = list()
    for line in fileinput.input(GUNICORN_SERVICE_FILE, inplace = True):
        line = line.strip()
        if len(line) == 0:
            print()
            continue

        originalLine = line

        key, sep, value = line.partition(GUNICORN_VARIABLE_SEP)
        value = envVariablesDict.get(key.casefold(), value)
        line = key + sep + value

        if line != originalLine:
            pair = (originalLine, line)
            changedPairs.append(pair)

        print(line)
    return changedPairs

def displayChangedLines(changedPairs):
    print("Count of updated lines in", GUNICORN_SERVICE_FILE, ":", len(changedPairs))
    for ctr, pair in enumerate(changedPairs, 1):
        print(ctr, end = ".\n")
        print(TAB + "From:", pair[0].strip())
        print(TAB + "To:  ", pair[1].strip())

envVariablesDict = getGunicornVariablesDict()
changedPairs = updateGunicornFromEnvVariables(envVariablesDict)
displayChangedLines(changedPairs)

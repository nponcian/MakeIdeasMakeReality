#!/usr/bin/env python3

# PURPOSE
# Fill-up the config/gunicorn.service with the missing values from the available variables set within
# the file config/environmentVariables. The script works by reading the configured environment
# variables, substituting the value of MIMR_GUNICORN_<NAME_OF_FIELD_HERE> where <NAME_OF_FIELD_HERE>
# is the name of the field (excluding the < >) in the gunicorn.service file. The names should be
# identical, not necessarily the case but the contents, including underscores if present.

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
INPUT_REQUEST_PREFIX = "---> Input:"
YES = "y"
NO = "n"
DISPLAY = "d"

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
        print("[", ctr, "]")
        print(TAB + "From:", pair[0].strip())
        print(TAB + "To:  ", pair[1].strip())

print("Updating", GUNICORN_SERVICE_FILE, "with the values set in", ENVIRONMENT_VARIABLES_FILE)
envVariablesDict = getGunicornVariablesDict()
changedPairs = updateGunicornFromEnvVariables(envVariablesDict)
displayChangedLines(changedPairs)

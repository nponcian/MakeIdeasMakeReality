#!/usr/bin/env python3

# PURPOSE
# Update the values set in the config/environmentVariables.

# USAGE
#     cd /path/to/makeIdeasMakeReality/
#     python3 script/environmentVariablesFiller.py

import os

ENVIRONMENT_VARIABLES_PATH="config/environmentVariables"
ENVIRONMENT_VARIABLES_SEP = "="

NEW_LINE = "\n"
INPUT_REQUEST_PREFIX = "---> Input:"
YES = "y"

def updateEnvVariables():
    temporaryFilePath = ENVIRONMENT_VARIABLES_PATH + "_temp"
    print("Leave blank to retain current value")

    with open(ENVIRONMENT_VARIABLES_PATH) as envVariablesFile:
        with open(temporaryFilePath, 'w') as temporaryFile:
            for line in envVariablesFile.readlines():
                line = line.strip()
                if len(line) == 0:
                    temporaryFile.write(NEW_LINE)
                    continue
                key, sep, value = line.partition(ENVIRONMENT_VARIABLES_SEP)
                print(INPUT_REQUEST_PREFIX, "{}{}".format(key, sep), end = "")
                updatedValue = input().strip()
                if len(updatedValue) != 0: value = updatedValue
                temporaryFile.write(key + sep + value + NEW_LINE)

    os.replace(temporaryFilePath, ENVIRONMENT_VARIABLES_PATH)

def displayEnvVariables():
    with open(ENVIRONMENT_VARIABLES_PATH) as envVariablesFile:
        print("Environment variables in", ENVIRONMENT_VARIABLES_PATH)
        for line in envVariablesFile.readlines():
            print("    ", line.strip())

displayEnvVariables()
print("Do you wish to update these environment variables? [y/n]")
print(INPUT_REQUEST_PREFIX, end = " ")
response = input().strip()
if response.casefold() == YES:
    updateEnvVariables()
    print("Successfully updated environment variables in", ENVIRONMENT_VARIABLES_PATH)
    displayEnvVariables()
else:
    print("Environment variables unchanged in", ENVIRONMENT_VARIABLES_PATH)

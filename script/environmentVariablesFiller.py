#!/usr/bin/env python3

# PURPOSE
# Update the values set in the config/environmentVariables.

# USAGE
#     cd /path/to/makeIdeasMakeReality/
#     python3 script/environmentVariablesFiller.py

import os

ENVIRONMENT_VARIABLES_FILE="config/environmentVariables"
ENVIRONMENT_VARIABLES_SEP = "="

NEW_LINE = "\n"
TAB = "    "
INPUT_REQUEST_PREFIX = "---> Input:"
YES = "y"

def displayEnvVariables():
    with open(ENVIRONMENT_VARIABLES_FILE) as envVariablesFile:
        print("Environment variables in", ENVIRONMENT_VARIABLES_FILE)
        for line in envVariablesFile.readlines():
            print(TAB + line.strip())

def updateEnvVariables():
    temporaryFileName = ENVIRONMENT_VARIABLES_FILE + "_temp"
    print("Unless you know what you are doing, only put a trailing / at the end of a path if the")
    print("initial default values also have it.")
    print("Leave blank to retain current value.")

    with open(ENVIRONMENT_VARIABLES_FILE) as envVariablesFile:
        with open(temporaryFileName, 'w') as temporaryFile:
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

    os.replace(temporaryFileName, ENVIRONMENT_VARIABLES_FILE)

displayEnvVariables()
print("You can choose to update", ENVIRONMENT_VARIABLES_FILE, "here or open it with a text editor.")
print("If you choose to update it here, there is always an option to redo any mistakes made at the end.")
print("If you choose to update it via a text editor, do it now before responding 'n' below.")
print("Do you wish to update these environment variables here? [y/n]")
print(INPUT_REQUEST_PREFIX, end = " ")
response = input().strip().casefold()

if response != YES:
    print("Environment variables left unchanged in", ENVIRONMENT_VARIABLES_FILE)

while response == YES:
    updateEnvVariables()
    print("Successfully updated environment variables in", ENVIRONMENT_VARIABLES_FILE)
    displayEnvVariables()

    print("Do you need to redo the editing? [y/n]")
    print(INPUT_REQUEST_PREFIX, end = " ")
    response = input().strip().casefold()

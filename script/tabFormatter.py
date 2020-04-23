#!/usr/bin/env python3

# PURPOSE
# Adjust the tab indentations used within a series of lines of text by a certain multiplier. One
# usecase for this are the snippets found in the website of bootstrap where a tab of size 2 is used.
# Making it 4 is what this script can do for you. It can also do the opposite, from 4 tab spaces to 2.

# USAGE
#     python3 /absolute/path/from/literally/anywhere/to/script/tabFormatter.py
#     or
#     python3 ../relative/path/from/literally/anywhere/to/script/tabFormatter.py

import sys

INPUT_REQUEST_PREFIX = "---> Input:"
INPUT_TERMINATOR = "\\q"
TAB_CHAR = " "
TAB_MULTIPLIER = 2

def getTargetMultiplier():
    print("Enter target tab multiplier:")
    print(" - Leave blank for the default value of", TAB_MULTIPLIER)
    print(" - For fraction multipliers (such as half), enter the floating value (e.g. 0.5)")
    print(INPUT_REQUEST_PREFIX, end = " ")
    targetMultiplier = input().strip()
    try:              targetMultiplier = float(targetMultiplier)
    except Exception: targetMultiplier = TAB_MULTIPLIER
    return targetMultiplier

def processInputLines(targetMultiplier):
    formattedString = str()

    print("Enter all lines to be formatted:")
    print("If done, press:", INPUT_TERMINATOR)
    print("      or press: Enter + Ctrl-D")
    for line in sys.stdin: # sys.stdin.readlines()
        if line.strip() == INPUT_TERMINATOR: break

        currentTabLength = len(line) - len(line.lstrip())
        updatedTabLength = int(currentTabLength * targetMultiplier)
        updatedTab = TAB_CHAR * updatedTabLength
        updatedLine = updatedTab + line[currentTabLength:]
        formattedString += updatedLine

    return formattedString

targetMultiplier = getTargetMultiplier()
formattedString = processInputLines(targetMultiplier)
print("Formatted string:")
print(formattedString)

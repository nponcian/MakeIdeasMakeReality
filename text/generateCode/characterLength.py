import random

DEFAULT_LENGTH = 12
MIN_MAX_LENGTH = (12, 15)

def getTargetLength():
    return random.randint(*MIN_MAX_LENGTH)

def getCharCountDivisionPerGroup(characterGroups, targetLength):
    return targetLength // len(characterGroups)

def getRemainingCharsCount(targetLength, currentChars):
    return targetLength - len(currentChars)

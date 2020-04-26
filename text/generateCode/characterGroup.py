import itertools
import random

from text.generateCode import ascii

def getCharacterGroups():
    characterGroups = list()
    characterGroups.append(ascii.getCharsSymbols())
    characterGroups.append(ascii.getChars("0", "9"))
    characterGroups.append(ascii.getChars("A", "Z"))
    characterGroups.append(ascii.getChars("a", "z"))
    return characterGroups

def shuffleCharacterGroups(characterGroups):
    for group in characterGroups:
        random.shuffle(group)

def getCharsPerGroup(characterGroups, targetCharCountPerGroup):
    charsFromTheGroups = list()
    for group in characterGroups:
        charsFromTheGroups += group[:targetCharCountPerGroup]
    return charsFromTheGroups

def getCharsFromRandomGroups(characterGroups, initialGroupsCharIndex, targetCharCount):
    randomChars = list()
    groupIdAndCharIndex = dict()
    for id, _ in enumerate(characterGroups):
        groupIdAndCharIndex[id] = initialGroupsCharIndex

    while len(randomChars) != targetCharCount:
        chosenGroupId = random.choice(list(groupIdAndCharIndex.keys()))
        chosenGroupCharacters = characterGroups[chosenGroupId]

        if groupIdAndCharIndex[chosenGroupId] >= len(chosenGroupCharacters):
            random.shuffle(chosenGroupCharacters) # shuffles characterGroups[chosenGroupId]
            groupIdAndCharIndex[chosenGroupId] = 0

        targetChar = chosenGroupCharacters[groupIdAndCharIndex[chosenGroupId]]
        randomChars.append(targetChar)

        groupIdAndCharIndex[chosenGroupId] += 1

    return randomChars

def shuffleIntoString(*args):
    combinedList = list(itertools.chain(*args))
    random.shuffle(combinedList)
    return "".join(combinedList)

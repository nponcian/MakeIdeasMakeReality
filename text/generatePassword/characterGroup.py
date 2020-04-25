import random

from text.generatePassword import ascii

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

def getCharsPerGroup(characterGroups, charCountLengthPerGroup):
    charsFromTheGroups = list()
    for group in characterGroups:
        charsFromTheGroups += group[:charCountLengthPerGroup]
    return charsFromTheGroups

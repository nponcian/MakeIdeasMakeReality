KEYCODE_FILLER_CHARS = "PoNcI"
MIN_REQUIRED_LENGTH = 5

def getDifferencesBetweenChars(keycode):
    keycodeLength = len(keycode)

    fillerCharCountNeeded = MIN_REQUIRED_LENGTH - keycodeLength
    if fillerCharCountNeeded > 0:
        keycode += KEYCODE_FILLER_CHARS[:fillerCharCountNeeded]
        keycodeLength = len(keycode)

    differencesList = list()
    for ctr in range(keycodeLength):
        currentCh = keycode[ctr]
        nextCh = keycode[ctr + 1] if ctr + 1 < keycodeLength else keycode[0]
        difference = ord(nextCh) - ord(currentCh)
        differencesList.append(difference)

    return differencesList

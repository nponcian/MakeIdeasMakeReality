from collections import (
    deque,
    namedtuple,
)

MinMaxRange = namedtuple("MinMaxRange", "min max")
ASCII_RANGE_TO_PROCESS = MinMaxRange(min = 32, max = 126)

def _isCharInRangeToProcess(value):
    charAsciiCode = value if isinstance(value, int) else ord(value)
    return ASCII_RANGE_TO_PROCESS.min <= charAsciiCode\
        and charAsciiCode <= ASCII_RANGE_TO_PROCESS.max

def _adjustCharValueToAllowedRange(chValue):
    while not _isCharInRangeToProcess(chValue):
        if chValue > ASCII_RANGE_TO_PROCESS.max:
            toShift = chValue - ASCII_RANGE_TO_PROCESS.max
            chValue = (ASCII_RANGE_TO_PROCESS.min - 1) + toShift
        else:
            toShift = ASCII_RANGE_TO_PROCESS.min - chValue
            chValue = (ASCII_RANGE_TO_PROCESS.max + 1) - toShift
    return chValue

def encrypt(textToCipher, keycodeDifferences):
    keycodeDifferences = deque(keycodeDifferences)

    encrypted = str()
    for ch in textToCipher:
        if not _isCharInRangeToProcess(ch):
            encrypted += ch
            continue

        differenceToUse = keycodeDifferences.popleft()
        keycodeDifferences.append(differenceToUse)

        newChValue = ord(ch) + differenceToUse
        newChValue = _adjustCharValueToAllowedRange(newChValue)

        encrypted += chr(newChValue)

    return encrypted

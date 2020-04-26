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

def decrypt(textToCipher, keycodeDifferences):
    keycodeDifferences = deque(keycodeDifferences)

    decrypted = str()
    for ch in textToCipher:
        if not _isCharInRangeToProcess(ch):
            decrypted += ch
            continue

        differenceToUse = keycodeDifferences.popleft()
        keycodeDifferences.append(differenceToUse)

        oldChValue = ord(ch) - differenceToUse
        while not _isCharInRangeToProcess(oldChValue):
            if oldChValue > ASCII_RANGE_TO_PROCESS.max:
                toShift = oldChValue - ASCII_RANGE_TO_PROCESS.max
                oldChValue = (ASCII_RANGE_TO_PROCESS.min - 1) + toShift
            else:
                toShift = ASCII_RANGE_TO_PROCESS.min - oldChValue
                oldChValue = (ASCII_RANGE_TO_PROCESS.max + 1) - toShift

        decrypted += chr(oldChValue)

    return decrypted

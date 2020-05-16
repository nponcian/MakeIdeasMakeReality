from collections import (
    deque,
    namedtuple,
)

from text.cipherMessage.algorithm import cipherAlgorithm

class KeycodeAddition(cipherAlgorithm.CipherAlgorithm):
    def __init__(self):
        super().__init__()

        MinMaxRange = namedtuple("MinMaxRange", "min max")
        self.ASCII_RANGE_TO_PROCESS = MinMaxRange(min = 32, max = 126)

        self.KEYCODE_FILLER_CHARS = "PoNcI"
        self.KEYCODE_MIN_LENGTH = 5

    def __isCharInRangeToProcess(self, value):
        charAsciiCode = value if isinstance(value, int) else ord(value)
        return self.ASCII_RANGE_TO_PROCESS.min <= charAsciiCode\
            and charAsciiCode <= self.ASCII_RANGE_TO_PROCESS.max

    def __shiftCharValueToAllowedRange(self, chValue):
        while not self.__isCharInRangeToProcess(chValue):
            if chValue > self.ASCII_RANGE_TO_PROCESS.max:
                toShift = chValue - self.ASCII_RANGE_TO_PROCESS.max
                chValue = (self.ASCII_RANGE_TO_PROCESS.min - 1) + toShift
            else:
                toShift = self.ASCII_RANGE_TO_PROCESS.min - chValue
                chValue = (self.ASCII_RANGE_TO_PROCESS.max + 1) - toShift
        return chValue

    def __getDifferencesBetweenChars(self, keycode):
        keycodeLength = len(keycode)

        fillerCharCountNeeded = self.KEYCODE_MIN_LENGTH - keycodeLength
        if fillerCharCountNeeded > 0:
            keycode += self.KEYCODE_FILLER_CHARS[:fillerCharCountNeeded]
            keycodeLength = len(keycode)

        differencesDeque = deque()
        for ctr in range(keycodeLength):
            currentCh = keycode[ctr]
            nextCh = keycode[ctr + 1] if ctr + 1 < keycodeLength else keycode[0]
            difference = ord(nextCh) - ord(currentCh)
            differencesDeque.append(difference)

        return differencesDeque

    def __cipher(self, message, keycode, cipherOperation):
        keycodeDifferences = self.__getDifferencesBetweenChars(keycode)

        ciphered = str()
        for ch in message:
            if not self.__isCharInRangeToProcess(ch):
                ciphered += ch
                continue

            differenceToUse = keycodeDifferences.popleft() # or use deque.rotate()
            keycodeDifferences.append(differenceToUse)

            expression = str("ord(ch) " + cipherOperation + " differenceToUse")
            chValue = eval(expression)
            chValue = self.__shiftCharValueToAllowedRange(chValue)

            ciphered += chr(chValue)

        return ciphered

    def encrypt(self, message, keycode):
        return self.__cipher(message, keycode, "+")

    def decrypt(self, message, keycode):
        return self.__cipher(message, keycode, "-")

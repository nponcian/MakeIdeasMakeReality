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

    def __adjustCharValueToAllowedRange(self, chValue):
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

    def encrypt(self, textToCipher, keycode):
        keycodeDifferences = self.__getDifferencesBetweenChars(keycode)

        encrypted = str()
        for ch in textToCipher:
            if not self.__isCharInRangeToProcess(ch):
                encrypted += ch
                continue

            differenceToUse = keycodeDifferences.popleft() # or use deque.rotate()
            keycodeDifferences.append(differenceToUse)

            newChValue = ord(ch) + differenceToUse
            newChValue = self.__adjustCharValueToAllowedRange(newChValue)

            encrypted += chr(newChValue)

        return encrypted

    def decrypt(self, textToCipher, keycode):
        keycodeDifferences = self.__getDifferencesBetweenChars(keycode)

        decrypted = str()
        for ch in textToCipher:
            if not self.__isCharInRangeToProcess(ch):
                decrypted += ch
                continue

            differenceToUse = keycodeDifferences.popleft()
            keycodeDifferences.append(differenceToUse)

            oldChValue = ord(ch) - differenceToUse
            oldChValue = self.__adjustCharValueToAllowedRange(oldChValue)

            decrypted += chr(oldChValue)

        return decrypted

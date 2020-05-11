import re

from text.commonWord.include import includerStrategy

SEPARATOR = " "

class Digits(includerStrategy.IncluderStrategy):
    def __init__(self):
        super().__init__()

    def reconstruct(self, text):
        if not text: return text
        text = text.casefold()
        text = self.__retainDigits(text)
        return text

    def __retainDigits(self, text):
        return re.sub("[^0-9]", SEPARATOR, text)

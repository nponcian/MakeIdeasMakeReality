import re

from text.commonWord.format import textFormatter

SEPARATOR = " "

class Digits(textFormatter.TextFormatter):
    def __init__(self):
        super().__init__()

    def reconstruct(self, text):
        if not text: return text
        text = text.casefold()
        text = self.__retainDigits(text)
        return text

    def __retainDigits(self, text):
        return re.sub("[^0-9]", SEPARATOR, text)

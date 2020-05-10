import re

from text.commonWord.format import textFormatter

SEPARATOR = " "

class Letters(textFormatter.TextFormatter):
    def __init__(self):
        super().__init__()

    def reconstruct(self, text):
        if not text: return text
        text = text.casefold()
        text = self.__retainLetters(text)
        return text

    def __retainLetters(self, text):
        return re.sub("[^a-zA-Z]", SEPARATOR, text)

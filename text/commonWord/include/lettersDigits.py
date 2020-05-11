import re

from text.commonWord.include import textFormatter

SEPARATOR = " "

class LettersDigits(textFormatter.TextFormatterStrategy):
    def __init__(self):
        super().__init__()

    def reconstruct(self, text):
        if not text: return text
        text = text.casefold()
        text = self.__retainLettersDigits(text)
        return text

    def __retainLettersDigits(self, text):
        return re.sub("[^a-zA-Z0-9]", SEPARATOR, text) # cannot use \w here as it includes _

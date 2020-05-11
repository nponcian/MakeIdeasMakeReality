import re

from text.commonWord.include import includerStrategy

SEPARATOR = " "

class Letters(includerStrategy.IncluderStrategy):
    def __init__(self):
        super().__init__()

    def reconstruct(self, text):
        if not text: return text
        text = text.casefold()
        text = self.__retainLetters(text)
        return text

    def __retainLetters(self, text):
        return re.sub("[^a-zA-Z]", SEPARATOR, text)

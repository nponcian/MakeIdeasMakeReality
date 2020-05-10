import re

from text.commonWord.format import textFormatter

SPLITTER_SYMBOLS = ",@|/:;()[]{}"
SPLITTER_SYMBOLS_IFF_WITH_SPACE = ".!?"
SEPARATOR = " "

class LettersDigitsNonsplitterSymbols(textFormatter.TextFormatter):
    def __init__(self):
        super().__init__()

    def reconstruct(self, text):
        if not text: return text
        text = text.casefold()
        text = self.__removeSplitters(text)
        text = self.__stripSplittersWithSpace(text)
        return text

    def __removeSplitters(self, text):
        return re.sub("[" + re.escape(SPLITTER_SYMBOLS) + "]", SEPARATOR, text)

    def __stripSplittersWithSpace(self, text):
        # google.cloud = ["google.cloud"]
        # google. cloud = ["google", "cloud"]
        updatedText = str()
        for word in text.split():
            strippedWord = word.strip(SPLITTER_SYMBOLS_IFF_WITH_SPACE)
            if len(strippedWord) > 0:
                updatedText += strippedWord + SEPARATOR
        return updatedText.rstrip()

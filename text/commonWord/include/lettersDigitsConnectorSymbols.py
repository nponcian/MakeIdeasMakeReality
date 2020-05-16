import re

from text.commonWord.include import includerStrategy

SYMBOLS_CONNECTING_WORDS = "-_'`.&+"
SEPARATOR = " "

class LettersDigitsConnectorSymbols(includerStrategy.IncluderStrategy):
    def __init__(self):
        super().__init__()

    def reconstruct(self, text):
        if not text: return text
        text = text.casefold()
        text = self.__removeNonConnectorSymbols(text)
        text = self.__stripConnectorSymbols(text)
        return text

    def __removeNonConnectorSymbols(self, text):
        return re.sub("[^\w" + re.escape(SYMBOLS_CONNECTING_WORDS) + "]", SEPARATOR, text)
        # or
        # filteredText = str()
        # for ch in text:
        #     if ch.isalnum() or ch in SYMBOLS_CONNECTING_WORDS:
        #         filteredText += ch
        #     else:
        #         filteredText += SEPARATOR
        # return filteredText

    def __stripConnectorSymbols(self, text):
        updatedText = str()
        for word in text.split():
            strippedWord = self.__stripNonAlNum(word)
            if len(strippedWord) > 0:
                updatedText += strippedWord + SEPARATOR
            # or using another logic via filter:
            # nonEmptyWords = list(filter(lambda word: len(word) > 0, words))
        return updatedText.rstrip()

    def __stripNonAlNum(self, word):
        substr = re.search("[a-zA-Z0-9].*[a-zA-Z0-9]", word)
        if substr: return substr.group(0)

        substr = re.search("[a-zA-Z0-9]", word)
        return substr.group(0) if substr is not None else ""

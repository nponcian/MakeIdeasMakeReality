SYMBOLS_CONNECTING_WORDS = "-_.'"
SEPARATOR = " "

from text.commonWord.format import textFormatter

class LettersDigitsConnectorSymbols(textFormatter.TextFormatter):
    def _removeSymbols(self, text):
        filteredText = str()
        for ch in text:
            if ch.isalnum() or ch in SYMBOLS_CONNECTING_WORDS:
                filteredText += ch
            else:
                filteredText += SEPARATOR
        return filteredText

    def reconstruct(self, text):
        if not text: return text
        text = text.casefold()
        text = self._removeSymbols(text)
        return text

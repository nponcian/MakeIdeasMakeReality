SYMBOLS_CONNECTING_WORDS = "-_.'"
SEPARATOR = " "

def _removeSymbols(text):
    filteredText = str()
    for ch in text:
        if ch.isalnum() or ch in SYMBOLS_CONNECTING_WORDS:
            filteredText += ch
        else:
            filteredText += SEPARATOR
    return filteredText

def reconstruct(text):
    if not text: return text
    text = text.casefold()
    text = _removeSymbols(text)
    return text

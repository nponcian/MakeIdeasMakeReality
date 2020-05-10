# NONE = ("none", "")
LETTERS = "letters"
LETTERS_DIGITS = "letters_digits:"
LETTERS_DIGITS_CONNECTORSYMBOLS = "letters_digits_connectorsymbols"
LETTERS_DIGITS_NONSPLITTERYMBOLS = "letters_digits_nonsplittersymbols"

from text.commonWord.format import (
    none,
    lettersDigitsConnectorSymbols,
)

defaultFormatter = none.NoneFormatter()
formatterDict =\
    {
        LETTERS_DIGITS_CONNECTORSYMBOLS : lettersDigitsConnectorSymbols.LettersDigitsConnectorSymbols()
    }

def create(formatType):
    if formatType in formatterDict:
        return formatterDict[formatType]

    return defaultFormatter

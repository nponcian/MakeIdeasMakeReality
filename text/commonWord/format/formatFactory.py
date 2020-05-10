from text.commonWord.format import (
    none,
    letters,
    lettersDigitsConnectorSymbols,
)

# format types
NONE = "none"
LETTERS = "letters"
LETTERS_DIGITS = "letters_digits:"
LETTERS_DIGITS_CONNECTORSYMBOLS = "letters_digits_connectorsymbols"
LETTERS_DIGITS_NONSPLITTERYMBOLS = "letters_digits_nonsplittersymbols"

formatterDict =\
    {
        NONE : none.NoneFormatter(),
        LETTERS : letters.Letters(),
        LETTERS_DIGITS_CONNECTORSYMBOLS : lettersDigitsConnectorSymbols.LettersDigitsConnectorSymbols()
    }

def getFormatter(formatType):
    if not formatType: formatType = NONE

    if formatType in formatterDict:
        return formatterDict[formatType]

    # TODO: raise an exception instead that will return a JSON error response with details of error
    return formatterDict[NONE]

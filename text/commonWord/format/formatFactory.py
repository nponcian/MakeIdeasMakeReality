from text.commonWord.format import (
    none,
    letters,
    digits,
    lettersDigits,
    lettersDigitsConnectorSymbols,
    lettersDigitsNonsplitterSymbols,
)

# format types
NONE = "none"
LETTERS = "letters"
DIGITS = "digits"
LETTERS_DIGITS = "letters_digits"
LETTERS_DIGITS_CONNECTORSYMBOLS = "letters_digits_connectorsymbols"
LETTERS_DIGITS_NONSPLITTERYMBOLS = "letters_digits_nonsplittersymbols"

formatterDict =\
    {
        NONE : none.NoneFormatter(),
        LETTERS : letters.Letters(),
        DIGITS : digits.Digits(),
        LETTERS_DIGITS : lettersDigits.LettersDigits(),
        LETTERS_DIGITS_CONNECTORSYMBOLS : lettersDigitsConnectorSymbols.LettersDigitsConnectorSymbols(),
        LETTERS_DIGITS_NONSPLITTERYMBOLS : lettersDigitsNonsplitterSymbols.LettersDigitsNonsplitterSymbols()
    }

def getFormatter(formatType):
    if not formatType: formatType = NONE

    if formatType in formatterDict:
        return formatterDict[formatType]

    # TODO: raise an exception instead that will return a JSON error indicating invalid input format
    return formatterDict[NONE]

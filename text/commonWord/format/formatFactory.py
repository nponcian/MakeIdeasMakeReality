from text.commonWord.format import (
    none,
    letters,
    digits,
    lettersDigits,
    lettersDigitsConnectorSymbols,
    lettersDigitsNonsplitterSymbols,
)

FORMATTER_DICT =\
    {
        "none" : none.NoneFormatter(),
        "letters" : letters.Letters(),
        "digits" : digits.Digits(),
        "letters_digits" : lettersDigits.LettersDigits(),
        "letters_digits_connectorsymbols" : lettersDigitsConnectorSymbols.LettersDigitsConnectorSymbols(),
        "letters_digits_nonsplittersymbols" : lettersDigitsNonsplitterSymbols.LettersDigitsNonsplitterSymbols()
    }

def getFormatter(formatType):
    NONE_KEY = "none"
    if formatType is None: formatType = NONE_KEY
    # TODO: raise an exception instead that will return a JSON error indicating invalid input format
    elif formatType not in FORMATTER_DICT: return FORMATTER_DICT[NONE_KEY]

    return FORMATTER_DICT[formatType]

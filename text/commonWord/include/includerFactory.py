from text.commonWord.include import (
    none,
    letters,
    digits,
    lettersDigits,
    lettersDigitsConnectorSymbols,
    lettersDigitsNonsplitterSymbols,
)

INCLUDER_DICT =\
    {
        "none" : none.NoneFormatter(),
        "letters" : letters.Letters(),
        "digits" : digits.Digits(),
        "letters_digits" : lettersDigits.LettersDigits(),
        "letters_digits_connectorsymbols" : lettersDigitsConnectorSymbols.LettersDigitsConnectorSymbols(),
        "letters_digits_nonsplittersymbols" : lettersDigitsNonsplitterSymbols.LettersDigitsNonsplitterSymbols()
    }

def getIncluder(includeType):
    NONE_KEY = "none"
    if includeType is None: includeType = NONE_KEY
    # TODO: raise an exception instead that will return a JSON error indicating invalid input format
    elif includeType not in INCLUDER_DICT: return INCLUDER_DICT[NONE_KEY]

    return INCLUDER_DICT[includeType]

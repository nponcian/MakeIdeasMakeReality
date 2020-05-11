from text.commonWord.include import (
    allChars,
    letters,
    digits,
    lettersDigits,
    lettersDigitsConnectorSymbols,
    lettersDigitsNonsplitterSymbols,
)

INCLUDER_DICT =\
    {
        "all" : allChars.AllChars(),
        "letters" : letters.Letters(),
        "digits" : digits.Digits(),
        "letters_digits" : lettersDigits.LettersDigits(),
        "letters_digits_connectorsymbols" : lettersDigitsConnectorSymbols.LettersDigitsConnectorSymbols(),
        "letters_digits_nonsplittersymbols" : lettersDigitsNonsplitterSymbols.LettersDigitsNonsplitterSymbols()
    }

def getIncluder(includeType):
    ALL_KEY = "all"
    if includeType is None: includeType = ALL_KEY
    # TODO: raise an exception instead that will return a JSON error indicating invalid input format
    elif includeType not in INCLUDER_DICT: return INCLUDER_DICT[ALL_KEY]

    return INCLUDER_DICT[includeType]

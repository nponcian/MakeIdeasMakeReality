import random

REPEAT_COUNT = 2
DISALLOWED_CHARS = [" ", '"', "'", "/", "\\", "`", "|"]
SYMBOL_CODE_RANGES = [(32, 47), (58, 64), (91, 96), (123, 126)]

def _getAsciiDecimalValue(variable):
    return variable if isinstance(variable, int) else ord(variable)

def _repeat(repeatCount):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result *= repeatCount
            return result
        return wrapper
    return decorator

@_repeat(REPEAT_COUNT)
def _getChars(start, end):
    start = _getAsciiDecimalValue(start)
    end = _getAsciiDecimalValue(end)
    return [chr(current) for current in range(start, end + 1) if chr(current) not in DISALLOWED_CHARS]

def _getCharsSymbols():
    return [ch for minMaxRange in SYMBOL_CODE_RANGES for ch in _getChars(*minMaxRange)]

def getCharacterGroups():
    characterGroups = list()
    characterGroups.append(_getCharsSymbols())
    characterGroups.append(_getChars("0", "9"))
    characterGroups.append(_getChars("A", "Z"))
    characterGroups.append(_getChars("a", "z"))
    return characterGroups

def shuffleCharacterGroups(characterGroups):
    for group in characterGroups:
        random.shuffle(group)

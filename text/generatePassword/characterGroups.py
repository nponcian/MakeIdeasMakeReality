REPEAT_COUNT = 2
DISALLOWED_CHARS = [" ", '"', "'", "/", "\\", "`", "|"]
SYMBOL_CODE_RANGES = [(32, 47), (58, 64), (91, 96), (123, 126)]

def getDecimalValue(variable):
    return variable if isinstance(variable, int) else ord(variable)

def repeat(repeatCount):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result *= repeatCount
            return result
        return wrapper
    return decorator

@repeat(2)
def getChars(start, end):
    start = getDecimalValue(start)
    end = getDecimalValue(end)
    return [chr(current) for current in range(start, end + 1) if chr(current) not in DISALLOWED_CHARS]

def getCharsSymbols():
    return [ch for minMaxRange in SYMBOL_CODE_RANGES for ch in getChars(*minMaxRange)]

def getCharacterGroups():
    characterGroups = list()
    characterGroups.append(getCharsSymbols())
    characterGroups.append(getChars("0", "9"))
    characterGroups.append(getChars("A", "Z"))
    characterGroups.append(getChars("a", "z"))
    return characterGroups

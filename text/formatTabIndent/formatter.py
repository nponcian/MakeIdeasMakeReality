DEFAULT_TAB_INDENT_MULTIPLIER = 2
TAB_CHAR = " "

def _floatOrDefault(targetMultiplier):
    try:              return float(targetMultiplier)
    except Exception: return DEFAULT_TAB_INDENT_MULTIPLIER

def formatTab(targetMultiplier, textToFormat):
    targetMultiplier = _floatOrDefault(targetMultiplier)
    formattedString = str()

    for line in textToFormat.splitlines(keepends = True): # for line in sys.stdin: # sys.stdin.readlines()
        if len(line.strip()) == 0:
            formattedString += line
            continue
        currentTabLength = len(line) - len(line.lstrip())
        updatedTabLength = int(currentTabLength * targetMultiplier)
        updatedTab = TAB_CHAR * updatedTabLength
        updatedLine = updatedTab + line[currentTabLength:]
        formattedString += updatedLine

    return formattedString

DEFAULT_TAB_INDENT_MULTIPLIER = 2
TAB_CHAR = " "
EXAMPLE_TEXT_TO_FORMAT = "\
<this>\n\
  <is>\n\
    <an>\n\
      example that contains\n\
      tab indents of size 2\n\
      <want to='make' the='tabindents: 4'?>\n\
        then, format me now!\n\
      </want>\n\
    </an>\n\
  </is>\n\
</this>"

def _floatOrDefault(tabMultiplier):
    try:              return float(tabMultiplier)
    except Exception: return DEFAULT_TAB_INDENT_MULTIPLIER

def formatTab(textToFormat, tabMultiplier):
    tabMultiplier = _floatOrDefault(tabMultiplier)
    formattedText = str()

    for line in textToFormat.splitlines(keepends = True): # for line in sys.stdin: # sys.stdin.readlines()
        if len(line.strip()) == 0:
            formattedText += line
            continue
        currentTabLength = len(line) - len(line.lstrip())
        updatedTabLength = int(currentTabLength * tabMultiplier)
        updatedTab = TAB_CHAR * updatedTabLength
        updatedLine = updatedTab + line[currentTabLength:]
        formattedText += updatedLine

    return formattedText

DEFAULT_TARGET_LINE_LENGTH = 100
DEFAULT_ROTATION_POINT = 3 # for Python comments
EXAMPLE_TEXT_TO_FORMAT = "\
# Sample line:\n\
# This is a line containing one hundred characters horizontally within this line ending in 3, 2, 111\n\
# This is another line containing more than one hundred characters horizontally within this line ending in 3, 2, 1\n\
# This is again another line, I would catch overflowing characters above, but even me would also overflow so let the next line handle me\n\
# Okay fine, I would catch their overflows here."

SPACE = " "
NEW_LINE = "\n"

def _prepareLine(rotationPointChars, prevOverflowingChars, line = ""):
    rotationPoint = len(rotationPointChars)
    if len(prevOverflowingChars) > 0 and len(line) > 0:
        prevOverflowingChars += SPACE
    return rotationPointChars + prevOverflowingChars + line[rotationPoint:]

def _updateLine(line, targetLineLength, rotationPoint):
    updatedLine = str()
    overflowingChars = str()

    if len(line) <= targetLineLength:
        updatedLine = line.rstrip() + NEW_LINE
    else:
        lastPossibleChar = line[targetLineLength - 1]
        firstOverflowingChar = line[targetLineLength]

        if lastPossibleChar.isspace() or firstOverflowingChar.isspace():
            updatedLine = line[:targetLineLength].rstrip() + NEW_LINE
            overflowingChars = line[targetLineLength:].strip()
        else:
            updatedLine = line[:targetLineLength]
            lastSpaceIndex = updatedLine.rfind(SPACE, rotationPoint + 1)
            lineBreaker = lastSpaceIndex if lastSpaceIndex > rotationPoint else targetLineLength

            updatedLine = line[:lineBreaker].rstrip() + NEW_LINE
            overflowingChars = line[lineBreaker:].strip()

    return updatedLine, overflowingChars

def limitLength(textToFormat, targetLineLength, rotationPoint):
    targetLineLength = int(targetLineLength)
    targetLineLength = targetLineLength if targetLineLength > 0 else DEFAULT_TARGET_LINE_LENGTH
    rotationPoint = int(rotationPoint) - 1 # base 0
    rotationPoint = rotationPoint if rotationPoint >= 0 else DEFAULT_ROTATION_POINT

    formattedText = str()
    prevOverflowingChars = str()

    for line in textToFormat.splitlines():
        line = _prepareLine(line[:rotationPoint], prevOverflowingChars, line)
        updatedLine, overflowingChars = _updateLine(line, targetLineLength, rotationPoint)

        formattedText += updatedLine
        prevOverflowingChars = overflowingChars

    rotationPointChars = textToFormat[:rotationPoint]
    while len(prevOverflowingChars) != 0:
        prevOverflowingChars = _prepareLine(rotationPointChars, prevOverflowingChars)
        updatedLine, overflowingChars = _updateLine(prevOverflowingChars, targetLineLength, rotationPoint)

        formattedText += updatedLine
        prevOverflowingChars = overflowingChars

    return formattedText

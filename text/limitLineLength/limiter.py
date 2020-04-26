# Note: Line strips only happen if chars are to be moved to the next line. Any tabbing or spacing
# made within a line would not be affected unless the words that they separate (specifically the
# word on the right side) is moved to the next line, in which case the spacing in between is
# stripped.

DEFAULT_TARGET_LINE_LENGTH = 100
DEFAULT_ROTATION_POINT = 1 # 3 for for Python comments
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

def _updateLine(line, targetLineLength, rotationPoint, shouldTerminateUnderflowingLines = True):
    updatedLine = str()
    overflowingChars = str()
    underflowingCount = 0

    if len(line) <= targetLineLength:
        updatedLine = line.rstrip()
        underflowingCount = targetLineLength - len(updatedLine) - 1 # 1 is for space
        if shouldTerminateUnderflowingLines or underflowingCount <= 0: updatedLine += NEW_LINE
    else:
        lastPossibleChar = line[targetLineLength - 1]
        firstOverflowingChar = line[targetLineLength]

        if lastPossibleChar.isspace() or firstOverflowingChar.isspace():
            updatedLine = line[:targetLineLength].rstrip() + NEW_LINE
            overflowingChars = line[targetLineLength:].strip()
        else:
            lastSpaceIndex = line[:targetLineLength].rfind(SPACE, rotationPoint + 1)
            lineBreaker = lastSpaceIndex if lastSpaceIndex > 0 else targetLineLength

            updatedLine = line[:lineBreaker].rstrip() + NEW_LINE
            overflowingChars = line[lineBreaker:].strip()

    # note that either overflow or underflow variable would be filled up at a time, but not both
    return updatedLine, overflowingChars, underflowingCount

def _processPrevUnderflow(line, rotationPoint, prevUnderflowingCount):
    if prevUnderflowingCount <= 0:  return line, "", 0

    appendToPrevLine = str()
    underflowingCount = 0

    underflowStart = rotationPoint
    underflowEnd = rotationPoint + prevUnderflowingCount
    lineFromRotationPointToEnd = line[rotationPoint:].strip()

    if len(lineFromRotationPointToEnd) <= prevUnderflowingCount:
        appendToPrevLine = SPACE + lineFromRotationPointToEnd.strip()
        underflowingCount = prevUnderflowingCount - len(appendToPrevLine)
        if underflowingCount <= 0: appendToPrevLine += NEW_LINE
        line = str()
    else:
        lastPossibleChar = line[underflowEnd - 1]
        firstOverflowingChar = line[underflowEnd]

        if lastPossibleChar.isspace() or firstOverflowingChar.isspace():
            appendToPrevLine = SPACE + line[underflowStart:underflowEnd].strip() + NEW_LINE
            line = line[:underflowStart] + line[underflowEnd:].strip()
        else:
            lineBreaker = line[:underflowEnd].rfind(SPACE, underflowStart + 1)

            if lineBreaker > 0:
                appendToPrevLine = SPACE + line[underflowStart:lineBreaker].strip()
                line = line[:underflowStart] + line[lineBreaker:].strip()

            appendToPrevLine += NEW_LINE

    return line, appendToPrevLine, underflowingCount

def limitLength(textToFormat, targetLineLength, rotationPoint):
    targetLineLength = int(targetLineLength)
    targetLineLength = targetLineLength if targetLineLength > 0 else DEFAULT_TARGET_LINE_LENGTH
    rotationPoint = int(rotationPoint) - 1 # base 0
    rotationPoint = rotationPoint if rotationPoint >= 0 else DEFAULT_ROTATION_POINT

    formattedText = str()
    prevOverflowingChars = str()

    for line in textToFormat.splitlines():
        line = _prepareLine(line[:rotationPoint], prevOverflowingChars, line)
        updatedLine, overflowingChars, _ = _updateLine(line, targetLineLength, rotationPoint)
        formattedText += updatedLine
        prevOverflowingChars = overflowingChars

    rotationPointChars = textToFormat[:rotationPoint]
    while len(prevOverflowingChars) != 0:
        prevOverflowingChars = _prepareLine(rotationPointChars, prevOverflowingChars)
        updatedLine, overflowingChars, _ = _updateLine(prevOverflowingChars, targetLineLength, rotationPoint)
        formattedText += updatedLine
        prevOverflowingChars = overflowingChars

    return formattedText

def limitAndCompressLength(textToFormat, targetLineLength, rotationPoint):
    targetLineLength = int(targetLineLength)
    targetLineLength = targetLineLength if targetLineLength > 0 else DEFAULT_TARGET_LINE_LENGTH
    rotationPoint = int(rotationPoint) - 1 # base 0
    rotationPoint = rotationPoint if rotationPoint >= 0 else DEFAULT_ROTATION_POINT

    formattedText = str()
    prevOverflowingChars = str()
    prevUnderflowingCount = 0

    for line in textToFormat.splitlines():
        line, appendToPrevLine, underflowingCount = _processPrevUnderflow(line, rotationPoint, prevUnderflowingCount)
        formattedText += appendToPrevLine
        prevUnderflowingCount = underflowingCount
        if len(line) == 0: continue

        line = _prepareLine(line[:rotationPoint], prevOverflowingChars, line)
        updatedLine, overflowingChars, underflowingCount = _updateLine(line, targetLineLength, rotationPoint, False)
        formattedText += updatedLine
        prevOverflowingChars = overflowingChars
        prevUnderflowingCount = underflowingCount

    rotationPointChars = textToFormat[:rotationPoint]
    while len(prevOverflowingChars) != 0:
        prevOverflowingChars = _prepareLine(rotationPointChars, prevOverflowingChars)
        updatedLine, overflowingChars, _ = _updateLine(prevOverflowingChars, targetLineLength, rotationPoint)
        formattedText += updatedLine
        prevOverflowingChars = overflowingChars

    return formattedText

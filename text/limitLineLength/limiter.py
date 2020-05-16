# Note: Line strips only happen if chars are to be moved to the next line. Any tabbing or spacing
# made within a line would not be affected unless the words that they separate (specifically the
# word on the right side) is moved to the next line, in which case the spacing in between is
# stripped.

DEFAULT_MAX_LINE_LENGTH = 100
DEFAULT_ROTATION_POINT = 1 # 3 for for Python comments
EXAMPLE_TEXT_TO_FORMAT = "\
# Enter paragraph here\n\
# Sample paragraph\n\
# Wrap the overflowing lines at point 3 to adjust for the tag '#'\n\
# This is a line containing exactly 100 characters, you can try to count this and you'd also get 100\n\
# This is another line containing more than 100 characters, don't manually count it, that is time consuming, use a text editor!\n\
# This is again another line, I would catch overflowing characters above, but even me would also overflow so let the next line handle me\n\
# Okay fine, I would catch their overflows here. Thisisanotherlinecontainingmorethan100charactersWITHOUTspaces,don'tmanuallycountit,thatistimeconsuming,useatexteditor!Thisisanotherlinecontainingmorethan100charactersWITHOUTspaces,don'tmanuallycountit,thatistimeconsuming,useatexteditor!"

SPACE = " "
NEW_LINE = "\n"

def _prepareLine(rotationPointChars, prevOverflowingChars, line = ""):
    rotationPoint = len(rotationPointChars)
    if len(prevOverflowingChars) > 0 and len(line) > 0:
        prevOverflowingChars += SPACE
    return rotationPointChars + prevOverflowingChars + line[rotationPoint:]

def _updateLine(line, maxLineLength, rotationPoint, shouldCompress):
    updatedLine = str()
    overflowingChars = str()
    underflowingCount = 0

    if len(line) <= maxLineLength:
        updatedLine = line.rstrip()
        underflowingCount = maxLineLength - len(updatedLine) - 1 # 1 is for space
        if not shouldCompress or underflowingCount <= 0: updatedLine += NEW_LINE
    else:
        lastPossibleChar = line[maxLineLength - 1]
        firstOverflowingChar = line[maxLineLength]

        if lastPossibleChar.isspace() or firstOverflowingChar.isspace():
            updatedLine = line[:maxLineLength].rstrip() + NEW_LINE
            overflowingChars = line[maxLineLength:].strip()
        else:
            lastSpaceIndex = line[:maxLineLength].rfind(SPACE, rotationPoint + 1)
            lineBreaker = lastSpaceIndex if lastSpaceIndex > 0 else maxLineLength

            updatedLine = line[:lineBreaker].rstrip() + NEW_LINE
            overflowingChars = line[lineBreaker:].strip()

    # note that either overflow or underflow variable would be filled up at a time, but not both
    return updatedLine, overflowingChars, underflowingCount

def _processPrevUnderflow(line, rotationPoint, prevUnderflowingCount):
    appendToPrevLine = str()
    underflowingCount = 0

    if prevUnderflowingCount <= 0:  return line, appendToPrevLine, underflowingCount

    lineFromRotationPointToEnd = line[rotationPoint:].strip()

    if len(lineFromRotationPointToEnd) <= prevUnderflowingCount:
        appendToPrevLine = SPACE + lineFromRotationPointToEnd.strip()
        underflowingCount = prevUnderflowingCount - len(appendToPrevLine)
        if underflowingCount <= 0: appendToPrevLine += NEW_LINE
        line = str()
    else:
        underflowStart = rotationPoint
        underflowEnd = rotationPoint + prevUnderflowingCount

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

def processLines(textToFormat, maxLineLength, rotationPoint, shouldCompress):
    maxLineLength = int(maxLineLength)
    maxLineLength = maxLineLength if maxLineLength > 0 else DEFAULT_MAX_LINE_LENGTH
    rotationPoint = int(rotationPoint) - 1 # base 0
    rotationPoint = rotationPoint if rotationPoint >= 0 else DEFAULT_ROTATION_POINT

    formattedText = str()
    prevOverflowingChars = str()
    prevUnderflowingCount = 0

    for line in textToFormat.splitlines():
        if shouldCompress:
            line, appendToPrevLine, underflowingCount = _processPrevUnderflow(line, rotationPoint, prevUnderflowingCount)
            formattedText += appendToPrevLine
            prevUnderflowingCount = underflowingCount
            if len(line) == 0: continue

        line = _prepareLine(line[:rotationPoint], prevOverflowingChars, line)
        updatedLine, overflowingChars, underflowingCount = _updateLine(line, maxLineLength, rotationPoint, shouldCompress)
        formattedText += updatedLine
        prevOverflowingChars = overflowingChars
        prevUnderflowingCount = underflowingCount

    rotationPointChars = textToFormat[:rotationPoint]
    while len(prevOverflowingChars) != 0:
        prevOverflowingChars = _prepareLine(rotationPointChars, prevOverflowingChars)
        updatedLine, overflowingChars, _ = _updateLine(prevOverflowingChars, maxLineLength, rotationPoint, shouldCompress)
        formattedText += updatedLine
        prevOverflowingChars = overflowingChars

    return formattedText

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

def limitLength(textToFormat, targetLineLength, rotationPoint):
    targetLineLength = int(targetLineLength)
    rotationPoint = int(rotationPoint) - 1 # base 0

    formattedText = str()
    overflowingChars = str()

    for line in textToFormat.splitlines():
        lineList = list(line)

        if len(overflowingChars) > 0:
            lineList[rotationPoint:] = list(overflowingChars) + [SPACE] + lineList[rotationPoint:]

        if len(lineList) <= targetLineLength:
            updatedLine = "".join(lineList).rstrip() + NEW_LINE
            overflowingChars = str()
        else:
            lastPossibleChar = lineList[targetLineLength - 1]
            firstOverflowingChar = lineList[targetLineLength]

            if lastPossibleChar.isspace() or firstOverflowingChar.isspace():
                updatedLine = "".join(lineList[:targetLineLength]).rstrip() + NEW_LINE
                overflowingChars = "".join(lineList[targetLineLength:]).strip()
            else:
                updatedLine = "".join(lineList[:targetLineLength])
                lastSpaceIndex = updatedLine.rfind(SPACE, rotationPoint + 1)
                lineBreaker = lastSpaceIndex if lastSpaceIndex > rotationPoint else targetLineLength

                updatedLine = "".join(lineList[:lineBreaker]).rstrip() + NEW_LINE
                overflowingChars = "".join(lineList[lineBreaker:]).strip()

        formattedText += updatedLine

    return formattedText

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

def formatLength(textToFormat, targetLineLength, rotationPoint):
    targetLineLength = int(targetLineLength)
    rotationPoint = int(rotationPoint) - 1 # base 0

    formattedText = str()
    overflowingChars = list()

    for line in textToFormat.splitlines():
        lineList = list(line)

        if len(overflowingChars) > 0:
            lineList[rotationPoint:] = overflowingChars + [SPACE] + lineList[rotationPoint:]

        currentLineChars = lineList[:targetLineLength] + [NEW_LINE]
        overflowingChars = lineList[targetLineLength:]

        formattedText += "".join(currentLineChars)

    return formattedText

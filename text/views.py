from django.shortcuts import render

from text.cipherMessage import algorithmsFactory
from text.formatTabIndent import formatter as tabIndentFormatter
from text.generateCode import (
    characterGroup,
    characterLength,
)
from text.limitLineLength import limiter as lineLengthLimiter

# Create your views here.

def text(request):
    template = "text/text.html"
    context = {}
    return render(request, template, context)

def countWord(request):
    template = "text/countWord.html"
    context = {}
    return render(request, template, context)

def cipherMessage(request):
    template = "text/cipherMessage.html"
    context = {}

    if request.method == "POST":
        keycode = request.POST.get("keycode", "")
        textToCipher = request.POST.get("textToCipher", "")
        isAnEncryptOperation = "encryptButton" in request.POST

        algorithm = algorithmsFactory.getChosenAlgorithm()
        cipheredText = algorithm.encrypt(textToCipher, keycode) if isAnEncryptOperation\
                        else algorithm.decrypt(textToCipher, keycode)

        context['keycode'] = keycode
        context['textToCipher'] = textToCipher
        context['cipheredText'] = cipheredText

    return render(request, template, context)

def formatTabIndent(request):
    template = "text/formatTabIndent.html"
    context = {
        "tabMultiplier" : tabIndentFormatter.DEFAULT_TAB_INDENT_MULTIPLIER,
        "textToFormatPlaceholder" : tabIndentFormatter.EXAMPLE_TEXT_TO_FORMAT
    }

    if request.method == "POST":
        tabMultiplier = request.POST.get("tabMultiplier", "")
        textToFormat = request.POST.get("textToFormat", "")
        formattedText = tabIndentFormatter.formatTab(textToFormat, tabMultiplier)

        context["tabMultiplier"] = tabMultiplier
        context["textToFormat"] = textToFormat
        context["formattedText"] = formattedText

    return render(request, template, context)

def generateCode(request):
    template = "text/generateCode.html"
    context = {}

    if request.method == "POST":
        groups = characterGroup.getCharacterGroups()
        characterGroup.shuffleCharacterGroups(groups)
        targetLength = characterLength.getTargetLength()
        charCountDivisionPerGroup = characterLength.getCharCountDivisionPerGroup(groups, targetLength)
        charsFromTheGroups = characterGroup.getCharsPerGroup(groups, charCountDivisionPerGroup)
        remainingCharsCount = characterLength.getRemainingCharsCount(targetLength, charsFromTheGroups)
        remainingChars = characterGroup.getCharsFromRandomGroups(groups,
                                                                charCountDivisionPerGroup,
                                                                remainingCharsCount)
        result = characterGroup.shuffleIntoString(charsFromTheGroups, remainingChars)
        context["generatedCode"] = result

    return render(request, template, context)

def limitLineLength(request):
    template = "text/limitLineLength.html"
    context = {
        "targetLineLength" : lineLengthLimiter.DEFAULT_TARGET_LINE_LENGTH,
        "rotationPoint" : lineLengthLimiter.DEFAULT_ROTATION_POINT,
        "textToFormatPlaceholder" : lineLengthLimiter.EXAMPLE_TEXT_TO_FORMAT
    }

    if request.method == "POST":
        targetLineLength = request.POST.get("targetLineLength", "")
        rotationPoint = request.POST.get("rotationPoint", "")
        textToFormat = request.POST.get("textToFormat", "")
        shouldCompress = "limitAndCompressButton" in request.POST

        formattedText = lineLengthLimiter.processLines(textToFormat,
                                                        targetLineLength,
                                                        rotationPoint,
                                                        shouldCompress)

        context["targetLineLength"] = targetLineLength
        context["rotationPoint"] = rotationPoint
        context["textToFormat"] = textToFormat
        context["formattedText"] = formattedText

    return render(request, template, context)

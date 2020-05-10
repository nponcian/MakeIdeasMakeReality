from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import permissions as restPermissions
from rest_framework import views as restViews
from rest_framework.response import Response

from service import permissions as servicePermissions
from text.cipherMessage import algorithmsFactory
from text.common import htmlToText
from text.commonWord import textGrouping
from text.commonWord.count import countHelper as commonWordCountHelper
from text.commonWord.format import formatFactory as commonWordFormatFactory
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

def commonWord(request):
    template = "text/commonWord.html"
    context = {}
    return render(request, template, context)

class CommonWordApi(restViews.APIView):
    permission_classes = [servicePermissions.DefaultServicePermission]

    # Not needed but to be able to post via the Django-restframework provided view thus added here
    def get(self, request, *args, **kwargs):
        return Response({"detail":"GET is unsupported, use POST with details on the body"})

    def post(self, request, *args, **kwargs):
        text = request.data.get("text", "")
        links = request.data.get("links", "")
        formatType = request.data.get("format", "")
        orderType = request.data.get("order", "")
        ignoreList = request.data.get("ignore", [])

        text += "\n" + htmlToText.htmlUrlsToText(*(links.strip().split()))
        text = text.strip()
        if len(text) == 0: return JsonResponse({})

        formatter = commonWordFormatFactory.getFormatter(formatType)
        text = formatter.reconstruct(text)

        groupedText = textGrouping.groupWords(text)

        wordsAndCountDict = commonWordCountHelper.count(groupedText)
        wordsAndCountDict = commonWordCountHelper.order(wordsAndCountDict, orderType)
        wordsAndCountDict = commonWordCountHelper.ignore(wordsAndCountDict, ignoreList)

        return Response(wordsAndCountDict) # JsonResponse(wordsAndCountDict)

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

from django.http import JsonResponse
from django.shortcuts import render
import json
from rest_framework import permissions as restPermissions
from rest_framework import views as restViews
from rest_framework.response import Response

from service import permissions as servicePermissions
from text.cipherMessage import algorithmsFactory
from text.common import htmlToText
from text.commonWord import textGrouping
from text.commonWord.count import countHelper as commonWordCountHelper
from text.commonWord.include import includerFactory as commonWordIncluderFactory
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

    # def get(self, request, *args, **kwargs):
    #     return Response({"detail":"GET is unsupported, use POST with details on the body"})

    def post(self, request, *args, **kwargs):
        text = request.data.get("text", "")
        file = request.FILES.get('file', None)
        urls = request.data.get("urls", [])
        include = request.data.get("include", "")
        order = request.data.get("order", "")
        ignore = request.data.get("ignore", [])

        # TODO: This, is currently bad. Future extensions will make this even worse. Design an input
        # chain handler, each getting their respective target data and each knowing what type of
        # data they are expecting. Put all user inputs to a single struct. Each handler in the chain
        # would act as builders. Each gradually building the struct to contain all user input data.
        # This function should only act as a facade! Don't put detailed-details here!
        if not isinstance(urls, list):
            urls = json.loads(urls)
            urls = list(filter(len, urls))
        if not isinstance(ignore, list):
            ignore = json.loads(ignore)
            ignore = list(filter(len, ignore))

        # TODO: Make different strategies to handle different file types. Add support for reading
        # pdf, doc, docx, html, images (should call a different service for text conversions), etc.
        if file: text += "".join([wordsChunk.decode() for wordsChunk in file.chunks()])
        text += "\n" + htmlToText.htmlUrlsToText(*urls) # if urls is str then # *(urls.split())
        text = text.strip()
        if len(text) == 0: return JsonResponse({})

        includer = commonWordIncluderFactory.getIncluder(include)
        text = includer.reconstruct(text)

        groupedText = textGrouping.groupWords(text)

        wordCountDict = commonWordCountHelper.count(groupedText)
        wordCountDict = commonWordCountHelper.ignore(wordCountDict, ignore)
        wordCountDictList = commonWordCountHelper.order(wordCountDict, order)

        return Response(wordCountDictList) # JsonResponse(wordCountDictList)

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

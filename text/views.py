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
from text.wrapLine import wrapper as lineWrapper

# Create your views here.

def text(request):
    template = "text/text.html"
    context = {}
    return render(request, template, context)

def cipherMessage(request):
    template = "text/cipherMessage.html"
    context = {}
    return render(request, template, context)

class CipherMessageApi(restViews.APIView):
    permission_classes = [servicePermissions.DefaultServicePermission]

    def post(self, request, *args, **kwargs):
        keycode = request.data.get("keycode", "")
        message = request.data.get("message", "")
        isADecryptOperation = request.data.get("operation", "") == "decrypt"

        algorithm = algorithmsFactory.getChosenAlgorithm()
        cipheredText = algorithm.decrypt(message, keycode) if isADecryptOperation\
                        else algorithm.encrypt(message, keycode)

        return Response(cipheredText)

def commonWord(request):
    template = "text/commonWord.html"
    context = {}
    return render(request, template, context)

class CommonWordApi(restViews.APIView):
    permission_classes = [servicePermissions.DefaultServicePermission]

    # def get(self, request, *args, **kwargs):
    #     return Response({"detail":"GET is unsupported, use POST with details on the body"})

    def post(self, request, *args, **kwargs):
        # TODO: Instead of doing everything below consecutively, with each step unnecessarily
        # waiting for the previous one, better yet implement asynchronus threading, somehow the same
        # idea with Map-Reduce algorithm. Handle each input type simultaneously in parallel then
        # just combine results in the end before sorting. This will alleviate the long processing of
        # htmlUrlsToText!

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

def formatTabIndent(request):
    template = "text/formatTabIndent.html"
    context = {
        "multiplier" : tabIndentFormatter.DEFAULT_TAB_INDENT_MULTIPLIER,
        "textToFormatPlaceholder" : tabIndentFormatter.EXAMPLE_TEXT_TO_FORMAT
    }
    return render(request, template, context)

class FormatTabIndentApi(restViews.APIView):
    permission_classes = [servicePermissions.DefaultServicePermission]

    def post(self, request, *args, **kwargs):
        multiplier = request.data.get("multiplier", "")
        text = request.data.get("text", "")
        formattedText = tabIndentFormatter.formatTab(text, multiplier)

        return Response(formattedText)

def generateCode(request):
    template = "text/generateCode.html"
    context = {}
    return render(request, template, context)

class GenerateCodeApi(restViews.APIView):
    permission_classes = [servicePermissions.DefaultServicePermission]

    def post(self, request, *args, **kwargs):
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
        return Response(result)

def wrapLine(request):
    template = "text/wrapLine.html"
    context = {
        "maxLineLength" : lineWrapper.DEFAULT_MAX_LINE_LENGTH,
        "rotationPoint" : lineWrapper.DEFAULT_ROTATION_POINT,
        "textToFormatPlaceholder" : lineWrapper.EXAMPLE_TEXT_TO_FORMAT
    }
    return render(request, template, context)

class WrapLineApi(restViews.APIView):
    permission_classes = [servicePermissions.DefaultServicePermission]

    def post(self, request, *args, **kwargs):
        maxLineLength = request.data.get("maxLineLength", lineWrapper.DEFAULT_MAX_LINE_LENGTH)
        rotationPoint = request.data.get("rotationPoint", lineWrapper.DEFAULT_ROTATION_POINT)
        text = request.data.get("text", "")
        shouldCompress = request.data.get("operation", "") == "limit_compress"

        formattedText = lineWrapper.processLines(text, maxLineLength, rotationPoint, shouldCompress)
        return Response(formattedText)

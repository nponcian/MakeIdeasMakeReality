from django.shortcuts import render

from text.generatePassword import (
    characterGroup,
    characterLength,
)

# Create your views here.

def text(request):
    template = "text/text.html"
    context = {}
    return render(request, template, context)

def generatePassword(request):
    groups = characterGroup.getCharacterGroups()
    characterGroup.shuffleCharacterGroups(groups)
    targetLength = characterLength.getTargetLength()
    charCountLengthPerGroup = characterLength.getCharCountLengthPerGroup(targetLength, groups)
    charsFromTheGroups = characterGroup.getCharsPerGroup(groups, charCountLengthPerGroup)

    template = "text/generatePassword.html"
    context = {}
    return render(request, template, context)

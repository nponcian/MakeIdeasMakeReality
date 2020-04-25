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
    template = "text/generatePassword.html"
    context = {}

    if request.method== "POST":
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
        context["generatedPassword"] = result

    return render(request, template, context)

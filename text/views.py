from django.shortcuts import render

from text.generatePassword import (
    characterGroups,
    passwordLength,
)

# Create your views here.

def text(request):
    template = "text/text.html"
    context = {}
    return render(request, template, context)

def generatePassword(request):
    groups = characterGroups.getCharacterGroups()
    characterGroups.shuffleCharacterGroups(groups)
    length = passwordLength.getTargetLength()

    template = "text/generatePassword.html"
    context = {}
    return render(request, template, context)

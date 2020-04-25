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
    print(characterGroups.getCharacterGroups())
    print(passwordLength.getPasswordLength())

    template = "text/generatePassword.html"
    context = {}
    return render(request, template, context)

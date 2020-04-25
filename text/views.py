from django.shortcuts import render

# Create your views here.

from text.generatePassword import characterGroups

def text(request):
    template = "text/text.html"
    context = {}
    return render(request, template, context)

def generatePassword(request):
    print(characterGroups.getCharacterGroups())
    template = "text/generatePassword.html"
    context = {}
    return render(request, template, context)

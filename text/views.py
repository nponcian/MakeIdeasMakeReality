from django.shortcuts import render

# Create your views here.

def text(request):
    template = "text/text.html"
    context = {}
    return render(request, template, context)

def generatePassword(request):
    template = "text/generatePassword.html"
    context = {}
    return render(request, template, context)

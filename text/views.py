from django.shortcuts import render

# Create your views here.

def text(request):
    template = "base.html"
    context = {}
    return render(request, template, context)

def generatePassword(request):
    template = "base.html"
    context = {}
    return render(request, template, context)

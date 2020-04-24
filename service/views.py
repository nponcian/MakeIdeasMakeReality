from django.shortcuts import render

# Create your views here.

def service(request):
    template = "service/service.html"
    context = {}
    return render(request, template, context)

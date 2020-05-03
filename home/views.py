from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def home(request):
    template = "home/home.html"
    context = {}
    return render(request, template, context)

def notFound(request, exception=None):
    print("Page not found for request", request, "with exception", exception)
    return HttpResponseNotFound("\
        <style>\
            .black{color:black;}\
            .red{color:red;}\
            .gold{color:gold;}\
        </style>\
        <h1><em class='black'>Ooops, tut mir leid, amigo!</em></h1>\
        <h2><code class='red'>We've already looked at the corners but can't find your request.</code></h2>\
        <h3><strong class='gold'>You could perhaps find something else interesting at <a href='/'>home</a>.</strong></h3>\
    ")

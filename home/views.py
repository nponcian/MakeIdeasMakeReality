from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hallo, Willkommen!")

def notFound(request):
    print("Page not found for request", request)
    return HttpResponse("\
        Ooops, tut mir leid!<br>\
        The resource you are looking for cannot be found.<br>\
        <br>\
        Go to <a href='/'>home</a> instead.\
    ")

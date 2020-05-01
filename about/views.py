from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.

def aboutMimr(request, *args):
    # Or simply # redirect("mimr/") # but don't put absolute "/mimr/" to retain the prefix "/about/"
    if args and args[0] == None: return redirect("about:aboutMimr", "mimr/")

    template = "about/aboutMimr.html"
    context = {}
    return render(request, template, context)

def whoAmI(request):
    template = "about/whoAmI.html"
    context = {}
    return render(request, template, context)

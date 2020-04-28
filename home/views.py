from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

import requests

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

def ipInfo(request):
    """
    Gets the external / public IP address of the server and the client.
    """

    # This returns the IP Address that was reached to access this server, so this only returns the
    # external IP address of this server if the request was sent to the external IP Address itself.
    # Sending a request to the local IP address (within the VPC) would also just return that local
    # IP address.
    # return JsonResponse({'ip' : request.META.get('HTTP_HOST', "")})

    SERVER_TAG = "server"
    CLIENT_TAG = "client"
    IP_ADDRESS_TAG = "ip_addr"

    SERVER_PUBLIC_IP_ADDRESS_FINDER = "http://ifconfig.me/ip"
    serverPublicIpResponse = requests.get(SERVER_PUBLIC_IP_ADDRESS_FINDER)
    serverPublicIp = serverPublicIpResponse.text
    serverInfo = {IP_ADDRESS_TAG : serverPublicIp}

    httpHeaderRemoteAddr = request.META.get("REMOTE_ADDR", "")
    httpHeaderXForwardedFor = request.META.get("HTTP_X_FORWARDED_FOR", "")
    clientPublicIp = httpHeaderRemoteAddr if httpHeaderRemoteAddr else httpHeaderXForwardedFor
    clientInfo = {IP_ADDRESS_TAG : clientPublicIp}

    return JsonResponse({SERVER_TAG : serverInfo, CLIENT_TAG : clientInfo})

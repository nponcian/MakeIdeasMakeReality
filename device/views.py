from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import requests

# Create your views here.

def device(request):
    return HttpResponse("This is device")

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
    WHO_QUERY_PARAM = "who"

    SERVER_PUBLIC_IP_ADDRESS_FINDER = "http://ifconfig.me/ip"
    serverPublicIpResponse = requests.get(SERVER_PUBLIC_IP_ADDRESS_FINDER)
    serverPublicIp = serverPublicIpResponse.text
    serverInfo = {IP_ADDRESS_TAG : serverPublicIp}

    httpHeaderRemoteAddr = request.META.get("REMOTE_ADDR", "")
    httpHeaderXForwardedFor = request.META.get("HTTP_X_FORWARDED_FOR", "")
    clientPublicIp = httpHeaderRemoteAddr if httpHeaderRemoteAddr else httpHeaderXForwardedFor
    clientInfo = {IP_ADDRESS_TAG : clientPublicIp}

    ipDict = {SERVER_TAG : serverInfo, CLIENT_TAG : clientInfo}

    who = request.GET.get(WHO_QUERY_PARAM)
    if who:
        who = who.casefold()
        if who == SERVER_TAG:   ipDict.pop(CLIENT_TAG, "")
        elif who == CLIENT_TAG: ipDict.pop(SERVER_TAG, "")

    return JsonResponse(ipDict)

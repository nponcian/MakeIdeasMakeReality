# Google Cloud: Cloud Function

# PURPOSE
# This is intended to be deployed and run on the Google Cloud: Cloud Functions platform to access
# the website for MakeIdeasMakeReality. Since the target website does not have a domain name
# (because domain names are not free!) and its external IP address is marked as ephemeral (only
# temporary, as reserving a static one is also not free!), this function is created to be the entry
# point to the website. This function would have a static URL provided by the GC Cloud Function
# platform itself that isn't changing and can be accessed anytime, thus users could always refer to
# this function to access the main site, even if the GC Compute Engine VM instance hosting the main
# site suddenly restarts and changes external IP address.

# FLOW
# This Cloud Function would communicate to the internal IP of the Compute Engine VM Instance through
# the configured Serverless VPC Access connector.
# 1. Client sends an HTTP request to the Cloud Function
# 2. Cloud Function receives the request via its domain name
# 3. Cloud Function has the information about the internal IP (within the VPC) of the Compute Engine
#    and the API endpoint to obtain the wanted information
# 4. Cloud Function sends the request through the Serverless VPC Access connector
# 5. Compute Engine receives the request via its internal IP address
# 6. Compute Engine gets its current external IP address
# 7. Compute Engine returns its external IP address to the Cloud Function
# 8 Cloud Function redirects the client to the current external IP of the MakeIdeasMakeReality website

from flask import redirect

import json
import requests

def redirectToSite(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.

    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'
    """

    PROTOCOL = "http://"
    COMPUTE_ENGINE_INTERNAL_IP = "10.128.0.2"
    API_ENDPOINT = "/api/ipinfo/?who=server"
    SERVER_TAG = "server"
    IP_ADDRESS_TAG = "ip_addr"

    apiRequest = PROTOCOL + COMPUTE_ENGINE_INTERNAL_IP + API_ENDPOINT
    response = requests.get(apiRequest)

    externalIpDict = json.loads(response.text)
    computeEngineExternalIp = externalIpDict[SERVER_TAG][IP_ADDRESS_TAG]

    targetSite = PROTOCOL + computeEngineExternalIp
    return redirect(targetSite)

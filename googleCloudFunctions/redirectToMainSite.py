# Google Cloud: Cloud Function

# PURPOSE
# This is intended to be deployed and run on the Google Cloud: Cloud Functions platform to access
# the website for MakeIdeasMakeReality. Since the target website does not have a domain name
# (because domain names are not free!) and its external IP address is marked as ephemeral (only
# temporary, as reserving a static one is also not free!), this function is created to be the entry
# point to the website. This function would have a static URL provided by the GC Cloud Function
# platform itself that would not change and can be accessed anytime, thus users could always refer
# to this function to access the main site, even if the GC Compute Engine VM instance hosting the
# main site suddenly restarts and changes external IP address. It is also possible to access other
# URLs of the main website by adding the query string ?q=put/target/path/here to the GC Cloud
# Function URL.

# PURPOSE (side note)
# If you're poor, you have no choice but to have a bit of creativity to stay alive, even if it means
# writing a dedicated GC Cloud Function just to stay free of charges :) But of course, with poverty
# comes hardships, and trade-offs, as the bad news is that this architecture introduces additional
# delays caused by the internal communications, additional requests and redirections, and a visible
# IP address, which would not happen if I was rich, coding inside my yacht. The good news? I don't
# have to bring my wallet out :)

# EXAMPLE URLS (using HTTP GET)
#     https://us-central1-makeideasmakereality.cloudfunctions.net/mimr
#     https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/wrapline
#     https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=api/ipinfo

# FLOW
# This Cloud Function would communicate to the internal IP of the Compute Engine VM Instance through
# the configured Serverless VPC Access connector.
# 1. Client sends an HTTP request to the Cloud Function
# 2. Cloud Function receives the request via its domain name
# 3. Cloud Function has the information about the internal IP (within the VPC) of the Compute Engine
#    and the API endpoint to obtain the wanted information
# 4. Cloud Function sends the request through the Serverless VPC Access connector. This means that,
#    one of the devices used in the VPC Access connector having an IP of one among the set range for
#    it would be used to send the request coming from the Cloud Function, and this IP would be the
#    "client IP" that is visible to the VM. So this could change for every request as the IPs are
#    within a range and not static.
# 5. Compute Engine receives the request which comes from one of the IPs in the range set for the
#    VPC Access connector and is sent to the VM's internal IP address within the internal VPC Network
# 6. Compute Engine gets its current external IP address
# 7. Compute Engine returns its external IP address to the Cloud Function
# 8. Cloud Function redirects the client to the current external IP of the MakeIdeasMakeReality website

from flask import redirect

import json
import requests

PROTOCOL = "http://"
COMPUTE_ENGINE_INTERNAL_IP = "10.128.0.2"
TARGET_PATH_TAG = "q"
SLASH = "/"

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

    if request.method == "GET": return handleGet(request)
    return handlePost(request)

def handleGet(request):
    API_ENDPOINT = "/service/device/ipinfo/api/?who=server"
    SERVER_TAG = "server"
    IP_ADDRESS_TAG = "ip_addr"

    apiRequest = PROTOCOL + COMPUTE_ENGINE_INTERNAL_IP + API_ENDPOINT
    response = requests.get(apiRequest)

    externalIpDict = json.loads(response.text)
    computeEngineExternalIp = externalIpDict[SERVER_TAG][IP_ADDRESS_TAG]

    targetPath = SLASH + request.args.get(TARGET_PATH_TAG, "").lstrip(SLASH)
    targetSite = PROTOCOL + computeEngineExternalIp + targetPath

    return redirect(targetSite)

def handlePost(request):
    targetPath = SLASH + request.args.get(TARGET_PATH_TAG, "").lstrip(SLASH)
    targetSite = PROTOCOL + COMPUTE_ENGINE_INTERNAL_IP + targetPath

    # Accept is like
    #     Here is my request and I would like (to Accept) this response format
    # Content-Type is like
    #     Here is my request (or response) and this (Content-Type) is the format of the content I am
    #     sending in my request (or response)
    targetHeaders = {'Content-Type': 'application/json', 'Accept':'application/json'}

    requestData = None
    content_type = request.headers['content-type']
    if content_type == 'application/json':
        requestData = request.get_json(silent=True)
    elif content_type == 'application/octet-stream':
        requestData = request.data
    elif content_type == 'text/plain':
        requestData = request.data
    elif content_type == 'application/x-www-form-urlencoded':
        requestData = request.form
    else:
        raise ValueError("Unknown content type: {}".format(content_type))

    print("handlePost content_type", content_type)
    print("handlePost requestData", type(requestData), requestData)

    response = requests.post(targetSite,
                            params = request.args,
                            headers = targetHeaders, # headers = request.headers,
                            data = json.dumps(requestData))
    # or
    # response = requests.post(targetSite, params = request.args, headers = targetHeaders, json = requestData)
    # or
    # response = requests.post(targetSite, params = request.args, json = requestData)

    return response.content # response.json()

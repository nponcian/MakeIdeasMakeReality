# PURPOSE
# To access the website for MakeIdeasMakeReality. Since the target website does not have a domain
# name and its external IP address is marked as ephemeral (temporary), this function is created to
# be the entry point to the main website. This would be deployed as a Google Cloud - Cloud Function,
# which would have a static domain name that isn't changing and can be accessed anytime.

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
    API_ENDPOINT = "/api/serverexternalip/"
    IP_ADDRESS_TAG = "ip_addr"

    print("eto1 start")
    apiRequest = PROTOCOL + COMPUTE_ENGINE_INTERNAL_IP + API_ENDPOINT
    response = requests.get(apiRequest)
    print("eto2", response)
    print("eto3", response.text)

    externalIpDict = json.loads(response.text)
    print("eto4", externalIpDict)
    computeEngineExternalIp = externalIpDict[IP_ADDRESS_TAG]

    targetSite = PROTOCOL + computeEngineExternalIp
    return redirect(targetSite)

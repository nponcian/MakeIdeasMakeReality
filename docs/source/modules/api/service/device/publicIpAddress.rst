.. _mimr-api-service-device-publicIpAddress:

Public IP Address
=================

.. toctree::
   :maxdepth: 1

Purpose
-------

Get the public IP address of your device.

Endpoint
--------

<SERVER_URL>/service/device/ipinfo/api

HTTP Method
-----------

GET

Parameters
----------

* ``who`` (optional, default is ``client``)

    Type
        string

    Description
        Whose IP address you want to get.

    Supported values:
        * client
            Request the IP Address of the client.

        * server
            Request the IP Address of the server.

    Example
        .. code-block::

            ?who=client

Run
---

**HTTP Request**::

    response=$(curl "https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/device/ipinfo/api&who=server")

    serverIp=$(echo "${response}" | tr -dc '0-9.')

    curl ${serverIp}/service/device/ipinfo/api?who=client # "?who=client" is optional

**HTTP Response**::

    {"client": {"ip_addr": "123.45.6.78"}}

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

https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/device/ipinfo/api

HTTP Method
-----------

GET

Parameters
----------

None

Run
---

**HTTP Request**::

    curl https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/device/ipinfo/api

**HTTP Response**::

    {"client": {"ip_addr": "123.45.6.78"}}

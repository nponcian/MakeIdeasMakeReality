.. _mimr-api-service-text-generateCode:

Generate Code
==============

.. toctree::
   :maxdepth: 1

Purpose
-------

Generate a random combination of letters, digits and symbols.

Endpoint
--------

https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/generatecode/api

HTTP Method
-----------

POST

.. note::

    It may seem that GET is a better option here as POST doesn't make sense considering that this service doesn't have any parameters and thus would not exceed the limit on URL length. But this would change in the future as additional control to the generated code would be implemented by adding parameters that could be lengthy. Thus, to prevent future changes to the API users, POST has been used as early as now.

Parameters
----------

None as of the moment

Run
---

**HTTP Request**::

    curl \
      --header "Content-Type: application/json" \
      --request POST \
      https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/generatecode/api

**HTTP Response**::

    "x%VZ4s^&k@9Mi>9"

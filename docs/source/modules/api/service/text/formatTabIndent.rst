.. _mimr-api-service-text-formatTabIndent:

Format Tab Indent
=================

.. toctree::
   :maxdepth: 1

Purpose
-------

Adjust the tab indentations per line of text.

Endpoint
--------

https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/formattabindent/api

HTTP Method
-----------

POST

Parameters
----------

* ``text``

    Type
        string

    Description
        Raw text input containing multiple lines of words, sentences and paragraphs containing indentations that would be adjusted.

    Example
        .. code-block::

            {"text":"<nav class="navbar navbar-light bg-light">\n  <a class="navbar-brand" href="#">\n    <img src="/docs/4.4/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="">\n    Bootstrap\n  </a>\n</nav>"}

* ``multiplier`` (optional, default is ``2``)

    Type
        number

            * float
            * greater than or equal to 0

    Description
        Used per line of ``text`` by multiplying the tab indentation spaces to the number indicated here. The resulting number would be the updated count of indentation spaces.

    Example
        .. code-block::

            {"multiplier":0.5}

Run
---

.. code-block::
    :caption: Input text
    :linenos:

    <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand" href="#">
        <img src="/docs/4.4/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="">
        Bootstrap
      </a>
    </nav>

**HTTP Request**::

    mySampleText='<nav class="navbar navbar-light bg-light">\n  <a class="navbar-brand" href="#">\n    <img src="/docs/4.4/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="">\n    Bootstrap\n  </a>\n</nav>'

    mySampleTextEscaped=$(echo "${mySampleText}" | sed 's/"/\\"/g') # escape the variable for it to be successfully parsed by the curl statement

    curlResultEscaped=$(\
        curl \
          --header "Content-Type: application/json" \
          --request POST \
          --data "{\"text\":\"${mySampleTextEscaped}\",\"multiplier\":2}" \
          https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/formattabindent/api)

    curlResult=$(echo "${curlResultEscaped}" | sed 's/\\"/"/g') # revert back the added escape symbols

    echo "${curlResult}"

**HTTP Response**::

    "<nav class="navbar navbar-light bg-light">\n    <a class="navbar-brand" href="#">\n        <img src="/docs/4.4/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="">\n        Bootstrap\n    </a>\n</nav>"

.. code-block::
    :caption: HTTP Response (displayed)
    :linenos:

    <nav class="navbar navbar-light bg-light">
        <a class="navbar-brand" href="#">
            <img src="/docs/4.4/assets/brand/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="">
            Bootstrap
        </a>
    </nav>

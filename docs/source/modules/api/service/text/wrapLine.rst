.. _mimr-api-service-text-wrapLine:

Wrap Line
=========

.. toctree::
   :maxdepth: 1

Purpose
-------

Limit the line length of a paragraph by wrapping the overflowing characters to a new line. Optionally, lines can also be compressed to fill-up any remaining spaces.

Endpoint
--------

https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/wrapline/api

HTTP Method
-----------

POST

Parameters
----------

* ``text``

    Type
        string

    Description
        Raw text input containing words, sentences and paragraphs that would be wrapped.

    Example
        .. code-block::

            {"text":"        # Enter paragraph here\n        # Sample paragraph\n        # Wrap the overflowing lines at point 11 to adjust for the indent and the tag #\n        # This is a line, containing exactly 100 characters, try to count this and you would get 100\n        # This is another line containing more than 100 characters, do not manually count it, that is time consuming, use a text editor!\n        # This is again another line, I would catch overflowing characters above, but even me would also overflow so let the next line handle me\n        # Okay fine, I would catch their overflows here. Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,thatistimeconsuming,useatexteditor!Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,thatistimeconsuming,useatexteditor!"}

* ``operation``

    Type
        string

    Description
        Indicate the type of wrapping operation to be done on ``text``.

    Supported values:
        * limit
            Limit each line's length by moving any exceeding characters to the next line.

        * limit_compress
            Limit each line's length by moving any exceeding characters to the next line. If a line does not exceed the ``maxLineLength``, any fitting words from the next line would be moved to occupy the remaining space.

    Example
        .. code-block::

            {"operation":"limit_compress"}

* ``maxLineLength`` (optional, default is ``100``)

    Type
        number

            * integer
            * greater than 0

    Description
        Maximum length per line of the result.

    Example
        .. code-block::

            {"maxLineLength":75}

* ``rotationPoint`` (optional, default is ``1``)

    Type
        number

            * integer
            * greater than 0

    Description
        1-based index to where the overflowing characters of the previous line would be placed on the next line. This is useful when wrapping code comments, to take into account the spacing and comment characters.

    Example
        .. code-block::

            {"rotationPoint":3}

Run
---

.. code-block::
    :caption: Input text
    :linenos:

            # Enter paragraph here
            # Sample paragraph
            # Wrap the overflowing lines at point 11 to adjust for the indent and the tag #
            # This is a line, containing exactly 100 characters, try to count this and you would get 100
            # This is another line containing more than 100 characters, do not manually count it, that is time consuming, use a text editor!
            # This is again another line, I would catch overflowing characters above, but even me would also overflow so let the next line handle me
            # Okay fine, I would catch their overflows here. Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,thatistimeconsuming,useatexteditor!Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,thatistimeconsuming,useatexteditor!

.. centered:: Limit

**HTTP Request**::

    curl \
      --header "Content-Type: application/json" \
      --request POST \
      --data '{"text":"        # Enter paragraph here\n        # Sample paragraph\n        # Wrap the overflowing lines at point 11 to adjust for the indent and the tag #\n        # This is a line, containing exactly 100 characters, try to count this and you would get 100\n        # This is another line containing more than 100 characters, do not manually count it, that is time consuming, use a text editor!\n        # This is again another line, I would catch overflowing characters above, but even me would also overflow so let the next line handle me\n        # Okay fine, I would catch their overflows here. Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,thatistimeconsuming,useatexteditor!Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,thatistimeconsuming,useatexteditor!","maxLineLength":100,"rotationPoint":11,"operation":"limit"}' \
      https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/ciphermessage/api

**HTTP Response**::

    "        # Enter paragraph here\n        # Sample paragraph\n        # Wrap the overflowing lines at point 11 to adjust for the indent and the tag #\n        # This is a line, containing exactly 100 characters, try to count this and you would get 100\n        # This is another line containing more than 100 characters, do not manually count it, that\n        # is time consuming, use a text editor! This is again another line, I would catch\n        # overflowing characters above, but even me would also overflow so let the next line handle\n        # me Okay fine, I would catch their overflows here.\n        # Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,that\n        # istimeconsuming,useatexteditor!Thisisaseriesofwordscontainingmorethan100charactersWITHOUTs\n        # paces,donotmanuallycountit,thatistimeconsuming,useatexteditor!\n"

.. code-block::
    :caption: HTTP Response (displayed)
    :linenos:

            # Enter paragraph here
            # Sample paragraph
            # Wrap the overflowing lines at point 11 to adjust for the indent and the tag #
            # This is a line, containing exactly 100 characters, try to count this and you would get 100
            # This is another line containing more than 100 characters, do not manually count it, that
            # is time consuming, use a text editor! This is again another line, I would catch
            # overflowing characters above, but even me would also overflow so let the next line handle
            # me Okay fine, I would catch their overflows here.
            # Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,that
            # istimeconsuming,useatexteditor!Thisisaseriesofwordscontainingmorethan100charactersWITHOUTs
            # paces,donotmanuallycountit,thatistimeconsuming,useatexteditor!

.. centered:: Limit and Compress

**HTTP Request**::

    curl \
      --header "Content-Type: application/json" \
      --request POST \
      --data '{"text":"        # Enter paragraph here\n        # Sample paragraph\n        # Wrap the overflowing lines at point 11 to adjust for the indent and the tag #\n        # This is a line, containing exactly 100 characters, try to count this and you would get 100\n        # This is another line containing more than 100 characters, do not manually count it, that is time consuming, use a text editor!\n        # This is again another line, I would catch overflowing characters above, but even me would also overflow so let the next line handle me\n        # Okay fine, I would catch their overflows here. Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,thatistimeconsuming,useatexteditor!Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,thatistimeconsuming,useatexteditor!","maxLineLength":100,"rotationPoint":11,"operation":"limit_compress"}' \
      https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/ciphermessage/api

**HTTP Response**::

    "        # Enter paragraph here Sample paragraph Wrap the overflowing lines at point 11 to adjust for\n        # the indent and the tag # This is a line, containing exactly 100 characters, try to count\n        # this and you would get 100 This is another line containing more than 100 characters, do\n        # not manually count it, that is time consuming, use a text editor! This is again another\n        # line, I would catch overflowing characters above, but even me would also overflow so let\n        # the next line handle me Okay fine, I would catch their overflows here.\n        # Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,that\n        # istimeconsuming,useatexteditor!Thisisaseriesofwordscontainingmorethan100charactersWITHOUTs\n        # paces,donotmanuallycountit,thatistimeconsuming,useatexteditor!"

.. code-block::
    :caption: HTTP Response (displayed)
    :linenos:

            # Enter paragraph here Sample paragraph Wrap the overflowing lines at point 11 to adjust for
            # the indent and the tag # This is a line, containing exactly 100 characters, try to count
            # this and you would get 100 This is another line containing more than 100 characters, do
            # not manually count it, that is time consuming, use a text editor! This is again another
            # line, I would catch overflowing characters above, but even me would also overflow so let
            # the next line handle me Okay fine, I would catch their overflows here.
            # Thisisaseriesofwordscontainingmorethan100charactersWITHOUTspaces,donotmanuallycountit,that
            # istimeconsuming,useatexteditor!Thisisaseriesofwordscontainingmorethan100charactersWITHOUTs
            # paces,donotmanuallycountit,thatistimeconsuming,useatexteditor!

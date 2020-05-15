.. _mimr-api-service-text-commonWord:

Common Words
============

.. toctree::
   :maxdepth: 1

Purpose
-------

Count the number of occurrences of each word in a document

HTTP Method
-----------

POST

Parameters
----------

* ``text`` (optional, default is ``""``)

    Type
        string

    Description
        Raw text input containing words, sentences and paragraphs that would directly be counted.

    Example
        .. code-block::

            {"text":"You are/somebody that I don't know\nBut you're takin' shots at me like it's Patron;And I'm just like, damn, (it's 7 AM)\nSay it:in|the_street, [that's a knock-out]\nBut you. say (it in} a Tweet, that's a cop-out\nAnd I'm just like, Hey,\tare you okay? {7 AM}"}

* ``file`` (optional, default is ``None``)

    .. note::

        This is only applicable to the GUI version.

    Type
        file

    Description
        File input uploaded to the GUI form. Contents of the file would be read and counted.

    Supported file formats
        #. Plain text-based file formats such as UTF-8 and ASCII text. Examples are .txt, .py, .cpp, .gitignore, .go, .html, .css, .js, .sh, and much more.

        .. note::

            PDF, MS Office (DOC, PPT, XLS, etc.), images (JPEG, PNG, etc.), audio, and video are not yet supported, but there is a plan to support them! Separate dedicated services that are focused on solely getting the text from its assigned types would be used.

* ``urls`` (optional, default is ``[]``)

    Type
        * list of strings
        * stringified list of strings

    Description
        List of URLs to be accessed via ``HTTP GET`` and then extracted of contents. Contents contain the real body of the webpage, without all the noise of html, css, and js tags.

    Example
        .. code-block::

            {"urls":['https://en.wikipedia.org/wiki/Atomic_bombings_of_Hiroshima_and_Nagasaki','https://www.lyricsfreak.com/b/beatles/when+im+sixty+four_10026687.html','https://www.django-rest-framework.org/api-guide/responses/','https://www.history.com/topics/american-civil-war/gettysburg-address']}

        .. code-block::

            {"urls":"['https://en.wikipedia.org/wiki/Atomic_bombings_of_Hiroshima_and_Nagasaki','https://www.lyricsfreak.com/b/beatles/when+im+sixty+four_10026687.html','https://www.django-rest-framework.org/api-guide/responses/','https://www.history.com/topics/american-civil-war/gettysburg-address']"}

* ``include`` (optional, default is ``"all"``)

    Type
        * string

    Description
        Indicate the type of characters to be taken into account from the source inputs during the formation and counting of words.

    Supported values:
        * all
            Include all kinds of characters in the source inputs.

        * letters
            Include only the letters in the source inputs. All non-letters are treated as blank spaces.

        * digits
            Include only the digits in the source inputs. All non-digits are treated as blank spaces.

        * letters_digits
            Include only the letters and digits in the source inputs. Everything else are treated as blank spaces.

        * letters_digits_connectorsymbols
            Include only the letters, digits, and connector symbols in the source inputs. Everything else are treated as blank spaces.

            Connector symbols are those that connect words. Specifically::

                -_'.&+

        * letters_digits_nonsplittersymbols
            Include only the letters, digits, and all symbols that are considered non-splitters in the source inputs. Splitter symbols are treated as blank spaces.

            Splitter symbols are those that separate words. Specifically::

                ,@|/:;()[]{}".!?

            .. note::

                The symbols ``.!?`` are only treated as "splitters" if and only if a space occurred before or after it. Thus, the ``.`` in ``sys.path`` is not a splitter which means ``sys.path`` remains as a single word while the ``.`` in ``sys. Path`` is considered a splitter, making sys and path from ``sys  Path`` as 2 different words.

    Example
        .. code-block::

            {"include":"letters_digits_nonsplittersymbols"}

* ``order`` (optional, default is ``"none"``)

    Type
        * string

    Description
        Sort the order of counted words.

    Supported values:
        * none
            No sorting. Order is arbitrary depending on hash values.

        * alphabetical
            Order the words alphabetically.

        * increasing
            Order by increasing count of word count. First item has the least count while the last item has the most count. Items that have the same count are sorted by word alphabetically.

        * decreasing
            Order by decreasing count of word count. First item has the most count while the last item has the least count. Items that have the same count are sorted by word alphabetically.

    Example
        .. code-block::

            {"order":"decreasing"}

* ``ignore`` (optional, default is ``[]``)

    Type
        * list of strings
        * stringified list of strings

    Description
        Specify the words that should not be counted.

    .. note::

        A special keyword ``"__DEFAULT__"`` can be added to the list. This signifies to remove the common prepositions and pronouns that might not be needed. `See them here`_.

    .. _See them here: https://storage.googleapis.com/mimr-bucket/text/assets/txt/commonWords.txt

    Example
        .. code-block::

            {"ignore":['i','hate','this','__DEFAULT__','word']}

        .. code-block::

            {"ignore":"['i','hate','this','__DEFAULT__','word']"}

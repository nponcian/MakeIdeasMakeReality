.. _mimr-api-service-text-commonWord:

Common Words
============

.. toctree::
   :maxdepth: 1

Purpose
-------

Count the number of occurrences of each word in a document

Endpoint
--------

https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/commonword/api

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

            {"urls":['https://en.wikipedia.org/wiki/Atomic_bombings_of_Hiroshima_and_Nagasaki','https://www.lyricsfreak.com/b/beatles/when+im+sixty+four_10026687.html','https://www.businessinsider.com.au/watch-live-spacex-crew-dragon-abort-test-nasa-2020-1','https://www.history.com/topics/american-civil-war/gettysburg-address']}

        .. code-block::

            {"urls":"['https://en.wikipedia.org/wiki/Atomic_bombings_of_Hiroshima_and_Nagasaki','https://www.lyricsfreak.com/b/beatles/when+im+sixty+four_10026687.html','https://www.businessinsider.com.au/watch-live-spacex-crew-dragon-abort-test-nasa-2020-1','https://www.history.com/topics/american-civil-war/gettysburg-address']"}

* ``include`` (optional, default is ``"all"``)

    Type
        * string

    Description
        Indicate the type of characters to be taken into account from the source inputs during the formation and counting of words.

    Supported values:
        * all
            Include all kinds of characters in the source inputs. So, for a sentence like ``You are you!``,
            the word ``you`` would be treated as a different word from ``you!``.

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

            .. note::

                All connector symbols are only considered as *"connectors"* if they actually connect words. Thus, the ``-`` in ``learn-it-all`` would make it remain as a single word while the ``-`` in ``-learn- all`` would be stripped into ``learn all``.

        * letters_digits_nonsplittersymbols
            Include only the letters, digits, and all symbols that are considered non-splitters in the source inputs. Splitter symbols are treated as blank spaces.

            Splitter symbols are those that separate words. Specifically::

                ,@|/:;()[]{}".!?

            .. note::

                The symbols ``.!?`` are only considered as *"splitters"* if and only if a space occurred before or after it. Thus, the ``.`` in ``sys.path`` is not a splitter which means ``sys.path`` remains as a single word while the ``.`` in ``sys. Path`` is considered a splitter, making sys and path from ``sys  Path`` as 2 different words.

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

            {"ignore":['\\','remove','all','^','__DEFAULT__','1','word','false','function','params','=','0']}

        .. code-block::

            {"ignore":"['\\','remove','all','^','__DEFAULT__','1','word','false','function','params','=','0']"}

Run
---

**HTTP Request**::

    curl \
      --header "Content-Type: application/json" \
      --request POST \
      --data '{"text":"You are/somebody that I don`t know\nBut you`re takin` shots at me like it`s Patron;And I`m just like, damn, (it`s 7 AM)\nSay it:in|the_street, [that`s a knock-out]\nBut you. say (it in} a Tweet, that`s a cop-out\nAnd I`m just like, Hey,\tare you okay? {7 AM}","urls":["https://en.wikipedia.org/wiki/Atomic_bombings_of_Hiroshima_and_Nagasaki","https://www.lyricsfreak.com/b/beatles/when+im+sixty+four_10026687.html","https://www.businessinsider.com.au/watch-live-spacex-crew-dragon-abort-test-nasa-2020-1","https://www.history.com/topics/american-civil-war/gettysburg-address"],"include":"letters_digits_nonsplittersymbols","order":"decreasing","ignore":["\\","remove","all","^","__DEFAULT__","1","word","false","function","params","=","0"]}' \
      https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/commonword/api

**HTTP Response**::

    [{"hiroshima":245},{"bidder":230},{"var":222},{"if":204},{"war":199},{"\\n":194},{"true":187},{"atomic":172},{"width":165},{"nagasaki":161},{"bomb":146},{"return":138},{"p":134},{"2":133},{"japanese":133},{"retrieved":130},{"topics":127},{"height":125},{"japan":123},{"new":123},{"color":122},{"august":118},{"pp":114},{"sizes":105},{"1945":96},{"300":95},{"bombing":94},{"index":94},{"www.history.com":94},{"link":93},{"maint":93},{"ref=harv":92},{"american-civil-war":91},{"&":90},{"display":90},{"background":89},{"zone":88},{"250":87},{"id":84},{"deferload":82},{"isoutstream":82},{"000":77},{"key":77},{"isbn":73},{"not":72},{"siteid":71},{"font-size":70},{"none":69},{"center":68},{"oclc":68},{"padding":68},{"mw-parser-output":67},{"b":65},{"s":63},{"88059007":62},{"would":62},{"adunitpath":61},{"bombings":61},{"city":61},{"world":61},{"0.1":60},{"90":60},{"after":59},{"10px":58},{"left":58},{"united":58},{"1px":57},{"history":57},{"0.10":55},{"air":55},{"nuclear":55},{"states":55},{"type":55},{"gettysburg":54},{"military":54},{"which":54},{"army":53},{"been":52},{"its":52},{"config":51},{"radiation":51},{"truman":51},{"use":51},{"3":50},{"about":50},{"effects":50},{"over":50},{"target":50},{"value":50},{"january":49},{"728":48},{"c":48},{"9":47},{"else":47},{"m":47},{"more":47},{"10":45},{"july":45},{"nativecardtype":45},{"during":44},{"hover":44},{"in_content":44},{"required":44},{"+":43},{"5":43},{"may":43},{"model":43},{"original":43},{"civil":42},{"e":42},{"ii":42},{"margin":42},{"one":42},{"solid":42},{"than":42},{"https":41},{"screensizes":41},{"simple":41},{"slotmodel":41},{"100%":40},{"4":40},{"bombs":40},{"press":40},{"two":40},{"u.s":40},{"#fff":39},{"tagid":39},{"2007":38},{"american":38},{"bidfloor":38},{"general":38},{"people":38},{"project":38},{"york":38},{"address":37},{"article":37},{"cities":37},{"june":37},{"placementid":37},{"survivors":37},...(trimmed)...]

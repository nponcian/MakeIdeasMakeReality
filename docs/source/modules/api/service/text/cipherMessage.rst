.. _mimr-api-service-text-cipherMessage:

Cipher Message
==============

.. toctree::
   :maxdepth: 1

Purpose
-------

Encrypt a message into an unreadable format using a user-provided keycode. Decrypt it back to its original form using the same keycode.

Endpoint
--------

https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/cipherMessage/api

HTTP Method
-----------

POST

Parameters
----------

* ``message``

    Type
        string

    Description
        Raw text input containing words, sentences and paragraphs that would directly be ciphered.

    Example
        .. code-block::

            {"message":"Hey, how are you? Use my credit card if you need it, card number is 1357 2468 9876 2345, expiry is 01/02, CVV is 666.\n\nAlso, I placed a cashbox at exactly 250 meters seabed-deep at coordinates 25.0000 N, 71.0000 W, the password is thiscontains2usd and it contains 2 USD."}

* ``operation``

    Type
        string

    Description
        Indicate the type of cipher operation to be done on ``message``.

    Supported values:
        * encrypt
            Convert the message to an unreadable format.

        * decrypt
            Convert the message back to the original format.

    Example
        .. code-block::

            {"operation":"encrypt"}

* ``keycode`` (optional, default is ``""``)

    .. warning::

        By using the default empty string, the text would still be processed into an unreadable format during encryption. But that is less secure, because decryption of the message would not require any keycode too!

    Type
        string

    Description
        To be used by the backend algorithms for uniquely transforming the ``message``.

    Example
        .. code-block::

            {"keycode":"thiscontains2usd... not 2thousand, not even 200, literally JUST 2!"}

Run
---

Encryption
^^^^^^^^^^

**HTTP Request**::

    curl \
      --header "Content-Type: application/json" \
      --request POST \
      --data '{"message":"Hey, how are you? Use my credit card if you need it, card number is 1357 2468 9876 2345, expiry is 01/02, CVV is 666.\n\nAlso, I placed a cashbox at exactly 250 meters seabed-deep at coordinates 25.0000 N, 71.0000 W, the password is thiscontains2usd and it contains 2 USD.","operation":"encrypt","keycode":"thiscontains2usd... not 2thousand, not even 200, literally JUST 2!"}' \
      https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/ciphermessage/api

**HTTP Response**::

    "<f${,gud(fw$cw`?? Gbf%x,bWykbW__``__u+Uae%tL1hx__`__2leaXlf |-Rlrq&9!kc1%n]g!;#A6&~<;=>|6(_ 2%#61+w[dpxwmviG$ 05=q12_g2gs{*#39\n\n2ybz,-OJ{jb/wSsU!mQ gh\\!%f3cci+ct^h!7@Bbalzc`!u;YPcjoruTn__``__2_t{W\\l}Uv]ltryJ=3/[B~$sO6oC04|855>;*p>heq_bx~*Rfk&ga-j0]bdtyZrXw%Dss`sNkopvc+c|t?lgo?2!sITN}"

Decryption
^^^^^^^^^^

**HTTP Request**::

    curl \
      --header "Content-Type: application/json" \
      --request POST \
      --data '{"message":"<f${,gud(fw$cw`?? Gbf%x,bWykbW__``__u+Uae%tL1hx__`__2leaXlf |-Rlrq&9!kc1%n]g!;#A6&~<;=>|6(_ 2%#61+w[dpxwmviG$ 05=q12_g2gs{*#39\n\n2ybz,-OJ{jb/wSsU!mQ gh\\!%f3cci+ct^h!7@Bbalzc`!u;YPcjoruTn__``__2_t{W\\l}Uv]ltryJ=3/[B~$sO6oC04|855>;*p>heq_bx~*Rfk&ga-j0]bdtyZrXw%Dss`sNkopvc+c|t?lgo?2!sITN}","operation":"decrypt","keycode":"thiscontains2usd... not 2thousand, not even 200, literally JUST 2!"}' \
      https://us-central1-makeideasmakereality.cloudfunctions.net/mimr?q=service/text/ciphermessage/api

**HTTP Response**::

    "Hey, how are you? Use my credit card if you need it, card number is 1357 2468 9876 2345, expiry is 01/02, CVV is 666.\n\nAlso, I placed a cashbox at exactly 250 meters seabed-deep at coordinates 25.0000 N, 71.0000 W, the password is thiscontains2usd and it contains 2 USD."

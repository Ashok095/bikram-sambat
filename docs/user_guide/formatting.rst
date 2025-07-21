.. _user_guide_formatting:

Formatting and Parsing
======================

The ``bikram_sambat`` library provides powerful tools for converting ``date``, ``time``, and ``datetime`` objects to and from strings.

Formatting with ``strftime``
----------------------------

The ``strftime`` method allows you to create a string representation of a ``date``, ``time``, or ``datetime`` object in a specific format. It supports all the standard ``strftime`` directives, plus some special directives for the Bikram Sambat calendar.

**Standard Directives**

Here are some of the most common standard directives:

* ``%Y``: Year with century (e.g., ``2081``)
* ``%y``: Year without century (e.g., ``81``)
* ``%m``: Month as a zero-padded decimal number (e.g., ``01``)
* ``%B``: Month as locale’s full name (e.g., ``Baishakh``)
* ``%b``: Month as locale’s abbreviated name (e.g., ``Bai``)
* ``%d``: Day of the month as a zero-padded decimal number (e.g., ``01``)
* ``%A``: Weekday as locale’s full name (e.g., ``Sunday``)
* ``%a``: Weekday as locale’s abbreviated name (e.g., ``Sun``)
* ``%H``: Hour (24-hour clock) as a zero-padded decimal number (e.g., ``13``)
* ``%I``: Hour (12-hour clock) as a zero-padded decimal number (e.g., ``01``)
* ``%p``: Locale’s equivalent of either AM or PM.
* ``%M``: Minute as a zero-padded decimal number (e.g., ``05``)
* ``%S``: Second as a zero-padded decimal number (e.g., ``09``)
* ``%Z``: Time zone name (if a time zone is specified).
* ``%z``: UTC offset in the form +HHMM or -HHMM.

**Bikram Sambat Specific Directives**

These directives allow you to format dates and times using Nepali numerals and names.

* ``%K``: Year in Nepali numerals (e.g., ``२०८१``)
* ``%N``: Month name in Nepali (e.g., ``वैशाख``)
* ``%D``: Day in Nepali numerals (e.g., ``०१``)
* ``%G``: Weekday name in Nepali (e.g., ``आइतबार``)
* ``%i``: Hour (12-hour clock) in Nepali numerals.
* ``%l``: Minute in Nepali numerals.
* ``%s``: Second in Nepali numerals.
* ``%P``: "AM/PM" in Nepali (e.g., ``पहिले`` for AM, ``पछि`` for PM).

**Examples**

.. code-block:: python

   from bikram_sambat import datetime

   dt = datetime(2081, 1, 1, 13, 30, 45)

   # Standard formatting
   print(dt.strftime("%Y-%m-%d %H:%M:%S"))
   print(dt.strftime("%A, %B %d, %Y"))

   # Nepali formatting
   print(dt.strftime("%K-%N-%D %i:%l:%s %P"))
   print(dt.strftime("%G, %N %D, %K"))

Parsing with ``fromstrftime`` (Not Yet Implemented)
---------------------------------------------------

The ``fromstrftime`` method, which will parse a string into a ``date``, ``time``, or ``datetime`` object, is planned for a future release.

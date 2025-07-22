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
   # >> 2081-01-01 13:30:45

   print(dt.strftime("%A, %B %d, %Y"))
   # >> Saturday, Baishakh 01, 2081


   # Nepali formatting
   print(dt.strftime("%K-%N-%D %i:%l:%s %P"))
   # >> २०८१-वैशाख-०१ ०१:३०:४५ पछिल्लो

   print(dt.strftime("%G, %N %D, %K"))
   # >> शनिबार, वैशाख ०१, २०८१


Parsing with ``fromstrftime``
-----------------------------

The ``fromstrftime`` method, which will parse a string into a ``date``, ``time``, or ``datetime`` object, is the reverse of `strftime`.

.. code-block:: python

    from bikram_sambat import datetime

    datetime_str = "2081-04-15 10:30:00"
    format_str = "%Y-%m-%d %H:%M:%S"
    dt = datetime.fromstrftime(datetime_str, format_str)
    print(dt)
    # >> 2081-04-15T10:30:00

   date_str_nepali = "शनिबार, वैशाख ०१, २०८१"
   format_str_date = "%G, %N %D, %K"
   parsed_date = date.fromstrftime(date_str_nepali, format_str_date)
   print(f"Parsed nepali date string '{date_str_nepali}': {parsed_date}")
   # >> Parsed nepali date string 'शनिबार, वैशाख ०१, २०८१': 2081-01-01

   dt_str = "2081-04-15 10:30 PM"
   format_str_dt = "%Y-%m-%d %I:%M %p"
   parsed_dt = datetime.fromstrftime(dt_str, format_str_dt)
   print(f"Parsed datetime string '{dt_str}': {parsed_dt}")
   # >> Parsed datetime string '2081-04-15 10:30 PM': 2081-04-15T22:30:00


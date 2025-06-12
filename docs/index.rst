.. bikram-sambat documentation master file

Welcome to bikram-sambat's documentation!
=========================================

A comprehensive, modern, and easy-to-use Python library for the Bikram Sambat (BS) calendar system.

``bikram-sambat`` provides a full suite of date and time objects that are **drop-in replacements** for Python's standard ``datetime`` library. It enables intuitive and accurate handling of the Nepali calendar, including date creation, arithmetic, formatting, and seamless conversion to and from the Gregorian (AD) calendar.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. Hiding the detailed table of contents for now, can be added later
.. introduction
.. installation
.. usage
.. api

Key Features
------------

* **Familiar ``datetime`` Interface**: Work with ``date``, ``time``, and ``datetime`` objects that subclass the standard library.
* **Accurate AD ⇔ BS Conversion**: Reliably convert between Gregorian (AD) and Bikram Sambat (BS) dates.
* **Rich Formatting & Parsing**: Full support for ``strftime`` and ``fromstrftime`` with custom directives for Nepali numerals (``२०८१``), English names (``Baishakh``), and Nepali Unicode names (``वैशाख``).
* **Full Timezone Support**: Create and manipulate timezone-aware ``time`` and ``datetime`` objects using ``pytz``.
* **Date & Time Arithmetic**: Perform all standard arithmetic operations with ``timedelta`` objects.

Quick Start
-----------

Here’s a quick tour of the ``bikram-sambat`` library's main features.

.. code-block:: python

   from bikram_sambat import date, datetime, timedelta, tz
   import datetime as pydt # Standard Python datetime for conversions

   # --- Date Operations ---

   # Create a BS date
   bs_date = date(2081, 4, 15) # Shrawan 15, 2081 B.S.
   print(f"BS Date: {bs_date}")
   # >> BS Date: 2081-04-15

   # Convert to Gregorian
   greg_date = bs_date.togregorian()
   print(f"Gregorian equivalent: {greg_date}")
   # >> Gregorian equivalent: 2024-07-30


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
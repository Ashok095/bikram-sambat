.. _user_guide_timezone:

Working with Timezones
======================

The ``bikram_sambat`` library provides robust support for timezones, allowing you to create timezone-aware ``time`` and ``datetime`` objects. This is essential for applications that need to handle time across different geographical regions.

Available Timezones
-------------------

The library comes with some common timezones built-in:

* ``tz.nepal``: Nepal Standard Time (Asia/Kathmandu, UTC+05:45).
* ``tz.utc``: Coordinated Universal Time.
* ``tz.india``: India Standard Time (Asia/Kolkata, UTC+05:30).

You can also get any timezone supported by the ``pytz`` library using the ``get_timezone`` function.

.. code-block:: python

   from bikram_sambat import tz

   # Access built-in timezones
   nepal_tz = tz.nepal
   utc_tz = tz.utc
   india_tz = tz.india

   print(f"Nepal Timezone: {nepal_tz}")
   # >> Nepal Timezone: Asia/Kathmandu

   print(f"UTC Timezone: {utc_tz}")
   # >> UTC Timezone: UTC

   print(f"India Timezone: {india_tz}")
   # >> India Timezone: Asia/Kolkata

   # Get a timezone by name
   new_york_tz = tz.get_timezone('America/New_York')
   print(f"New York Timezone: {new_york_tz}")
    # >> New York Timezone: America/New_York

Creating Timezone-Aware Objects
-------------------------------

To make a ``time`` or ``datetime`` object timezone-aware, pass a ``tzinfo`` object to its constructor.

.. code-block:: python

   from bikram_sambat import datetime, time, tz

   # Create a timezone-aware datetime in Nepal
   dt_nepal = datetime(2081, 1, 1, 10, 0, 0, tzinfo=tz.nepal)
   print(f"Aware datetime in Nepal: {dt_nepal}")
   # >> Aware datetime in Nepal: 2081-01-01T10:00:00+05:45


   # Create a timezone-aware time in New York
   t_ny = time(10, 0, 0, tzinfo=tz.get_timezone('America/New_York'))
   print(f"Aware time in New York: {t_ny}")
   # >> Aware time in New York: 10:00:00

   dt_ny = datetime(2081, 1, 1, 10, 0, 0, tzinfo=tz.get_timezone('America/New_York'))
   print(f"Aware datetime in New York: {dt_ny}")
   # >> Aware datetime in New York: 2081-01-01T10:00:00-05:00


Converting Between Timezones
----------------------------

You can easily convert a timezone-aware ``datetime`` object to another timezone using the ``astimezone`` method.

.. code-block:: python

   from bikram_sambat import datetime, tz

   # Create a datetime in Nepal time
   dt_nepal = datetime(2081, 1, 1, 10, 0, 0, tzinfo=tz.nepal)
   print(f"Datetime in Nepal: {dt_nepal}")
   # >> Datetime in Nepal: 2081-01-01T10:00:00+05:45

   # Convert to UTC
   dt_utc = dt_nepal.astimezone(tz.utc)
   print(f"Datetime in UTC: {dt_utc}")
   # >> Datetime in UTC: 2081-01-01T04:15:00+00:00

   # Convert to New York time
   dt_ny = dt_nepal.astimezone(tz.get_timezone('America/New_York'))
   print(f"Datetime in New York: {dt_ny}")
   # >> Datetime in New York: 2081-01-01T00:15:00-04:00

Naive vs. Aware Objects
-----------------------

A ``datetime`` or ``time`` object is "naive" if it does not have any timezone information associated with it. It's "aware" if it does. It's generally recommended to work with aware objects to avoid ambiguity.

.. code-block:: python

   from bikram_sambat import datetime

   # A naive datetime
   dt_naive = datetime(2081, 1, 1, 10, 0, 0)
   print(f"Is naive? {dt_naive.tzinfo is None}")
   # >> Is naive? True

   # An aware datetime
   from bikram_sambat import tz
   dt_aware = datetime(2081, 1, 1, 10, 0, 0, tzinfo=tz.nepal)
   print(f"Is aware? {dt_aware.tzinfo is not None}")
   # >> Is aware? True
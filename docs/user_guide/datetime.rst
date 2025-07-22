.. _user_guide_datetime:

Working with Datetimes
======================

The ``bikram_sambat.datetime`` object combines a ``date`` and a ``time``, representing a specific moment in time. It's a subclass of Python's ``datetime.datetime``.

Creating a Datetime
-------------------

You can create a ``datetime`` object by providing the year, month, day, hour, minute, second, and microsecond.

.. code-block:: python

   from bikram_sambat import datetime

   # Create a specific datetime
   dt = datetime(2081, 1, 1, 10, 30, 45, 123456)
   print(f"Datetime: {dt}")
   # >> Datetime: 2081-01-01T10:30:45.123456

You can also get the current datetime in the Bikram Sambat calendar using the ``now()`` class method.

.. code-block:: python

   from bikram_sambat import datetime

   # Get the current naive datetime
   now_naive = datetime.now()
   print(f"Current naive datetime: {now_naive}")
   # >> Current naive datetime: 2082-04-06T01:49:00.367176


   # Get the current aware datetime in a specific timezone
   from bikram_sambat import tz
   now_aware = datetime.now(tz.nepal)
   print(f"Current aware datetime in Nepal: {now_aware}")
   # >> Current aware datetime in Nepal: 2082-04-06T07:34:00.368572+0545

Accessing Datetime Components
-----------------------------

You can access all the components of a ``datetime`` object:

.. code-block:: python

   from bikram_sambat import datetime

   dt = datetime(2081, 4, 15, 10, 30, 45)

   print(f"Year: {dt.year}")
   # >> Year: 2081

   print(f"Month: {dt.month}")
   # >> Month: 4

   print(f"Day: {dt.day}")
   # >> Day: 15

   print(f"Hour: {dt.hour}")
   # >> Hour: 10

   print(f"Minute: {dt.minute}")
   # >> Minute: 30

   print(f"Second: {dt.second}")
   # >> Second: 45


Datetime Arithmetic
-------------------

You can perform arithmetic on ``datetime`` objects using ``timedelta`` objects.

.. code-block:: python

   from bikram_sambat import datetime, timedelta

   dt = datetime(2081, 1, 1, 12, 0, 0)
   delta = timedelta(days=10, hours=5)

   future_dt = dt + delta
   past_dt = dt - delta

   print(f"10 days and 5 hours after {dt} is {future_dt}")
   # >> 10 days and 5 hours after 2081-01-01T12:00:00 is 2081-01-11T17:00:00

   print(f"10 days and 5 hours before {dt} is {past_dt}")
   # >> 10 days and 5 hours before 2081-01-01T12:00:00 is 2080-12-21T07:00:00

You can also find the difference between two datetimes:

.. code-block:: python

   from bikram_sambat import datetime

   dt1 = datetime(2081, 1, 1, 12, 0, 0)
   dt2 = datetime(2081, 1, 11, 17, 0, 0)

   diff = dt2 - dt1
   print(f"The difference between {dt1} and {dt2} is {diff}")
   # >> The difference between 2081-01-01T12:00:00 and 2081-01-11T17:00:00 is 10 days, 5:00:00



Timezones
---------

See the :ref:`user_guide_timezone` section for more details on working with timezones.

Converting to and from Gregorian Datetimes
------------------------------------------

See the :ref:`user_guide_conversion` section for more details.

Formatting Datetimes
--------------------

See the :ref:`user_guide_formatting` section for more details on how to format datetimes as strings.

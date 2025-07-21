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

You can also get the current datetime in the Bikram Sambat calendar using the ``now()`` class method.

.. code-block:: python

   from bikram_sambat import datetime

   # Get the current naive datetime
   now_naive = datetime.now()
   print(f"Current naive datetime: {now_naive}")

   # Get the current aware datetime in a specific timezone
   from bikram_sambat import tz
   now_aware = datetime.now(tz.nepal)
   print(f"Current aware datetime in Nepal: {now_aware}")

Accessing Datetime Components
-----------------------------

You can access all the components of a ``datetime`` object:

.. code-block:: python

   from bikram_sambat import datetime

   dt = datetime(2081, 4, 15, 10, 30, 45)

   print(f"Year: {dt.year}")
   print(f"Month: {dt.month}")
   print(f"Day: {dt.day}")
   print(f"Hour: {dt.hour}")
   print(f"Minute: {dt.minute}")
   print(f"Second: {dt.second}")

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
   print(f"10 days and 5 hours before {dt} is {past_dt}")

You can also find the difference between two datetimes:

.. code-block:: python

   from bikram_sambat import datetime

   dt1 = datetime(2081, 1, 1, 12, 0, 0)
   dt2 = datetime(2081, 1, 11, 17, 0, 0)

   diff = dt2 - dt1
   print(f"The difference between {dt1} and {dt2} is {diff}")

Timezones
---------

See the :ref:`user_guide_timezone` section for more details on working with timezones.

Converting to and from Gregorian Datetimes
------------------------------------------

See the :ref:`user_guide_conversion` section for more details.

Formatting Datetimes
--------------------

See the :ref:`user_guide_formatting` section for more details on how to format datetimes as strings.

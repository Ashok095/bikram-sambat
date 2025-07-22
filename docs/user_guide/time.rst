.. _user_guide_time:

Working with Time
=================

The ``bikram_sambat.time`` object represents a time of day, independent of any particular date. It's a subclass of Python's ``datetime.time``.

Creating a Time
---------------

You can create a ``time`` object by providing the hour, minute, second, and microsecond.

.. code-block:: python

   from bikram_sambat import time

   # Create a specific time
   t = time(10, 30, 45, 123456)
   print(f"Time: {t}")
   # >> Time: 10:30:45.123456

Accessing Time Components
-------------------------

You can access the components of a ``time`` object:

.. code-block:: python

   from bikram_sambat import time

   t = time(10, 30, 45, 123456)

   print(f"Hour: {t.hour}")
   # >> Hour: 10

   print(f"Minute: {t.minute}")
   # >> Minute: 30

   print(f"Second: {t.second}")
   # >> Second: 45

   print(f"Microsecond: {t.microsecond}")
   # >> Microsecond: 123456

Timezones
---------

You can create timezone-aware ``time`` objects by passing a ``tzinfo`` object. See the :ref:`user_guide_timezone` section for more details.

.. code-block:: python

   from bikram_sambat import time, tz

   # Create a naive time
   naive_time = time(10, 30)
   print(f"Naive time: {naive_time}")
   # >> Naive time: 10:30:00

   # Create a timezone-aware time
   aware_time = time(10, 30, tzinfo=tz.nepal)
   print(f"Aware time: {aware_time}")
   # >> Aware time: 10:30:00+05:45

.. note::
   For a `time`-only object, calculating the UTC offset for timezones with Daylight Saving Time (DST) requires a reference date. This library uses the current system date for this calculation. Therefore, the UTC offset (`%z`) for a `time` object may vary depending on the day the code is run.

Formatting Times
----------------

You can format ``time`` objects as strings using the ``strftime`` method. See the :ref:`user_guide_formatting` section for more details.

.. _user_guide_timedelta:

Working with Timedeltas
=======================

A ``bikram_sambat.timedelta`` object represents a duration, the difference between two dates or times. It's a subclass of Python's ``datetime.timedelta``, so it works in exactly the same way.

Creating a Timedelta
--------------------

You can create a ``timedelta`` object by specifying the duration in days, seconds, microseconds, milliseconds, minutes, hours, or weeks.

.. code-block:: python

   from bikram_sambat import timedelta

   # A duration of 10 days
   delta1 = timedelta(days=10)
   print(f"Delta 1: {delta1}")
   # >> Delta 1: 10 days, 0:00:00

   # A duration of 5 hours and 30 minutes
   delta2 = timedelta(hours=5, minutes=30)
   print(f"Delta 2: {delta2}")
   # >> Delta 2: 5:30:00

   # A complex duration
   delta3 = timedelta(weeks=2, days=3, hours=4, minutes=5, seconds=6, milliseconds=7, microseconds=8)
   print(f"Delta 3: {delta3}")
   # >> Delta 3: 17 days, 4:05:06.007008

Timedelta Arithmetic
--------------------

You can perform arithmetic with ``timedelta`` objects.

.. code-block:: python

   from bikram_sambat import timedelta

   delta1 = timedelta(days=1)
   delta2 = timedelta(hours=12)

   # Add two timedeltas
   total_delta = delta1 + delta2
   print(f"{delta1} + {delta2} = {total_delta}")
   # >> 1 day, 0:00:00 + 12:00:00 = 1 day, 12:00:00

   # Subtract two timedeltas
   diff_delta = delta1 - delta2
   print(f"{delta1} - {delta2} = {diff_delta}")
   # >> 1 day, 0:00:00 - 12:00:00 = 12:00:00

   # Multiply a timedelta by a number
   multiplied_delta = delta1 * 2
   print(f"{delta1} * 2 = {multiplied_delta}")
   # >> 1 day, 0:00:00 * 2.5 = 2 days, 12:00:00

   # Divide a timedelta by a number
   divided_delta = delta1 / 2
   print(f"{delta1} / 2 = {divided_delta}")
   # >> 1 day, 0:00:00 / 2 = 12:00:00

Using Timedeltas with Dates and Datetimes
-----------------------------------------

The primary use of ``timedelta`` objects is to perform arithmetic with ``date`` and ``datetime`` objects. See the :ref:`user_guide_date` and :ref:`user_guide_datetime` sections for more details.

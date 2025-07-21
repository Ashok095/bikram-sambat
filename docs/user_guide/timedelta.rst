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

   # A duration of 5 hours and 30 minutes
   delta2 = timedelta(hours=5, minutes=30)
   print(f"Delta 2: {delta2}")

   # A complex duration
   delta3 = timedelta(weeks=2, days=3, hours=4, minutes=5, seconds=6, milliseconds=7, microseconds=8)
   print(f"Delta 3: {delta3}")

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

   # Subtract two timedeltas
   diff_delta = delta1 - delta2
   print(f"{delta1} - {delta2} = {diff_delta}")

   # Multiply a timedelta by a number
   multiplied_delta = delta1 * 2
   print(f"{delta1} * 2 = {multiplied_delta}")

   # Divide a timedelta by a number
   divided_delta = delta1 / 2
   print(f"{delta1} / 2 = {divided_delta}")

Using Timedeltas with Dates and Datetimes
-----------------------------------------

The primary use of ``timedelta`` objects is to perform arithmetic with ``date`` and ``datetime`` objects. See the :ref:`user_guide_date` and :ref:`user_guide_datetime` sections for more details.

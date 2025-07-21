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

Accessing Time Components
-------------------------

You can access the components of a ``time`` object:

.. code-block:: python

   from bikram_sambat import time

   t = time(10, 30, 45, 123456)

   print(f"Hour: {t.hour}")
   print(f"Minute: {t.minute}")
   print(f"Second: {t.second}")
   print(f"Microsecond: {t.microsecond}")

Timezones
---------

You can create timezone-aware ``time`` objects by passing a ``tzinfo`` object. See the :ref:`user_guide_timezone` section for more details.

.. code-block:: python

   from bikram_sambat import time, tz

   # Create a naive time
   naive_time = time(10, 30)
   print(f"Naive time: {naive_time}")

   # Create a timezone-aware time
   aware_time = time(10, 30, tzinfo=tz.nepal)
   print(f"Aware time: {aware_time}")

Formatting Times
----------------

You can format ``time`` objects as strings using the ``strftime`` method. See the :ref:`user_guide_formatting` section for more details.

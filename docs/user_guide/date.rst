.. _user_guide_date:

Working with Dates
==================

The ``bikram_sambat.date`` object is the cornerstone of handling dates in the Bikram Sambat calendar. It's designed to feel familiar to Python's built-in ``datetime.date``, so you can get started quickly.

Creating a Date
---------------

Creating a new ``date`` object is as simple as providing the year, month, and day.

.. code-block:: python

   from bikram_sambat import date

   # Create a specific date (New Year's Day 2081 BS)
   new_year_2081 = date(2081, 1, 1)
   print(f"New Year's Day 2081 BS: {new_year_2081}")

   # Another example (a date in the middle of the year)
   some_day = date(2080, 5, 15)
   print(f"A specific day: {some_day}")

You can also get today's date in the Bikram Sambat calendar using the ``today()`` class method.

.. code-block:: python

   from bikram_sambat import date

   # Get today's date
   today_bs = date.today()
   print(f"Today's date in BS is: {today_bs}")

Accessing Date Components
-------------------------

Once you have a ``date`` object, you can easily access its components:

.. code-block:: python

   from bikram_sambat import date

   d = date(2081, 4, 15)

   print(f"Year: {d.year}")
   print(f"Month: {d.month}")
   print(f"Day: {d.day}")

Comparing Dates
---------------

You can compare two ``date`` objects using the standard comparison operators.

.. code-block:: python

   from bikram_sambat import date

   date1 = date(2081, 1, 1)
   date2 = date(2081, 1, 2)
   date3 = date(2081, 1, 1)

   print(f"{date1} < {date2}: {date1 < date2}")
   print(f"{date1} == {date3}: {date1 == date3}")

Date Arithmetic
---------------

You can perform arithmetic on ``date`` objects using ``timedelta`` objects.

.. code-block:: python

   from bikram_sambat import date, timedelta

   d = date(2081, 1, 1)
   delta = timedelta(days=10)

   future_date = d + delta
   past_date = d - delta

   print(f"10 days after {d} is {future_date}")
   print(f"10 days before {d} is {past_date}")

You can also find the difference between two dates:

.. code-block:: python

   from bikram_sambat import date

   date1 = date(2081, 1, 1)
   date2 = date(2081, 1, 11)

   diff = date2 - date1
   print(f"The difference between {date1} and {date2} is {diff.days} days.")

Converting to and from Gregorian Dates
--------------------------------------

See the :ref:`user_guide_conversion` section for more details.

Formatting Dates
----------------

See the :ref:`user_guide_formatting` section for more details on how to format dates as strings.

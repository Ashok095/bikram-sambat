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
   # >> New Year's Day 2081 BS: 2081-01-01

   # Another example (a date in the middle of the year)
   some_day = date(2080, 5, 15)
   print(f"A specific day: {some_day}")
   # >> A specific day: 2080-05-15

You can also get today's date in the Bikram Sambat calendar using the ``today()`` class method.

.. code-block:: python

   from bikram_sambat import date

   # Get today's date
   today_bs = date.today()
   print(f"Today's date in BS is: {today_bs}")
   # >> Today's date in BS is: 2082-04-06

Accessing Date Components
-------------------------

Once you have a ``date`` object, you can easily access its components:

.. code-block:: python

   from bikram_sambat import date

   d = date(2081, 4, 15)

   print(f"Year: {d.year}")
   # >> Year: 2081

   print(f"Month: {d.month}")
   # >> Month: 4

   print(f"Day: {d.day}")
   # >> Day: 15

Comparing Dates
---------------

You can compare two ``date`` objects using the standard comparison operators.

.. code-block:: python

   from bikram_sambat import date

   date1 = date(2081, 1, 1)
   date2 = date(2081, 1, 2)
   date3 = date(2081, 1, 1)

   print(f"{date1} < {date2}: {date1 < date2}")
   # >> 2081-01-01 < 2081-01-02: True
   print(f"{date1} == {date3}: {date1 == date3}")
   # >> 2081-01-01 == 2081-01-01: True

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
   # >> 10 days after 2081-01-01 is 2081-01-11

   print(f"10 days before {d} is {past_date}")
   # >> 10 days before 2081-01-01 is 2080-12-21



You can also find the difference between two dates:

.. code-block:: python

   from bikram_sambat import date

   date1 = date(2081, 1, 1)
   date2 = date(2081, 1, 11)

   diff = date2 - date1
   print(f"The difference between {date1} and {date2} is {diff.days} days.")
   # >> The difference between 2081-01-01 and 2081-01-11 is 10 days.
   
Converting to and from Gregorian Dates
--------------------------------------

See the :ref:`user_guide_conversion` section for more details.

Formatting Dates
----------------

See the :ref:`user_guide_formatting` section for more details on how to format dates as strings.

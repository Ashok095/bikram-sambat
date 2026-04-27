.. _user_guide_calendar:

Calendar Generation System
==========================

The ``bikram_sambat`` library provides a powerful calendar generation system that allows you to create structural mappings between Bikram Sambat (BS) and Gregorian (AD) dates. This is particularly useful for building UI components like date pickers, printable calendars, or data synchronization tools.

BS Calendar Generation
----------------------

The ``bs_calendar()`` function generates a comprehensive mapping for a given BS year and month. It returns a ``CalendarMonthData`` object containing details about every single day in that month.

.. code-block:: python

   from bikram_sambat import bs_calendar

   # Get calendar data for Baishakh 2081 BS
   cal = bs_calendar(year=2081, month=1)

   print(f"Year: {cal.bs_year}, Month: {cal.bs_month}")
   # >> Year: 2081, Month: 1

   # Access the first day of the month
   first_day = cal.days[0]
   print(f"BS: {first_day.bs_year}-{first_day.bs_month}-{first_day.bs_day}")
   print(f"AD: {first_day.ad_full_date}")
   # >> BS: 2081-1-1
   print(f"Weekday: {first_day.week_day}") 
   # >> Weekday: 6 (Saturday)

If you omit the ``month`` parameter, it returns a list of ``CalendarMonthData`` objects for the entire BS year.

AD Calendar Generation
----------------------

Similarly, ``ad_calendar()`` allows you to generate a BS mapping starting from the first day of a Gregorian (AD) month.

.. code-block:: python

   from bikram_sambat import ad_calendar

   # Get calendar data starting from April 2024 (AD)
   cal = ad_calendar(year=2024, month=4)

   print(f"AD Year: {cal.ad_year}, AD Month: {cal.ad_month}")
   # >> AD Year: 2024, AD Month: 4
   print(f"Starts in BS: {cal.bs_year}-{cal.bs_month}")
   # >> Starts in BS: 2080-12

Month Matrix Generation
-----------------------

For UI layouts, the ``monthcalendar()`` function returns a matrix (list of lists) representing the month's grid, similar to the standard Python ``calendar.monthcalendar``.

.. code-block:: python

   from bikram_sambat import monthcalendar

   # Generate a 2D matrix for Baishakh 2081
   matrix = monthcalendar(2081, 1)

   for week in matrix:
       print(week)
   
   # >> [0, 0, 0, 0, 0, 0, 1]
   # >> [2, 3, 4, 5, 6, 7, 8]
   # ...
   
   # Note: The matrix starts on Sunday. Zeros represent days 
   # belonging to the previous or next month.

JSON Serialization
------------------

All calendar data models (``CalendarMonthData`` and ``CalendarDayData``) include a ``to_dict()`` method, making it easy to convert the data to a format suitable for JSON serialization in web applications.

.. code-block:: python

   import json
   from bikram_sambat import bs_calendar

   cal = bs_calendar(2083, 1)
   
   # Convert to a dictionary and dump to JSON
   print(json.dumps(cal.to_dict(), indent=2))

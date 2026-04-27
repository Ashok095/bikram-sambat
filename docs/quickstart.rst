.. _quickstart:

Quickstart
==========

This guide provides a brief overview of the ``bikram-sambat`` library's main features.

.. code-block:: python

   from bikram_sambat import date, datetime, timedelta, tz
   import datetime as pydt # Standard Python datetime for conversions

   # --- Date Operations ---

   # Create a BS date
   bs_date = date(2081, 4, 15) # Shrawan 15, 2081 B.S.
   print(f"BS Date: {bs_date}")
   # >> BS Date: 2081-04-15

   # Convert to Gregorian
   greg_date = bs_date.togregorian()
   print(f"Gregorian equivalent: {greg_date}")
   # >> Gregorian equivalent: 2024-07-30

   # --- Datetime Operations ---

   # Create a timezone-aware BS datetime in Nepal
   bs_dt_aware = datetime(2081, 5, 1, 10, 30, tzinfo=tz.nepal)
   print(f"Aware BS Datetime: {bs_dt_aware}")
   # >> Aware BS Datetime: 2081-05-01T10:30:00+05:45

   # Format in Nepali
   formatted = bs_dt_aware.strftime("%G, %N %D, %K साल, %i:%l %P")
   print(f"Formatted in Nepali: {formatted}")
   # >> Formatted in Nepali: बुधवार, भदौ १६, २०८१ साल, १०:३० पूर्वाह्न

   # --- Arithmetic ---

   # Perform arithmetic between two fixed dates
   start_date = date(2081, 12, 1) # Chaitra 1, 2081
   end_of_year = date(2081, 12, 30) # End of Chaitra
   days_left = end_of_year - start_date
   print(f"Days from {start_date} to {end_of_year}: {days_left.days}")
   # >> Days from 2081-12-01 to 2081-12-30: 29

   # --- Calendar Generation System ---
   from bikram_sambat import bs_calendar, monthcalendar

   # Get a day-by-day calendar mapping for a BS month
   bs_cal = bs_calendar(year=2080, month=1)
   print(f"BS Month 2080-01 has {len(bs_cal.days)} days.")
   # >> BS Month 2080-01 has 31 days.

   # Get a matrix for UI rendering (like python's calendar.monthcalendar)
   matrix = monthcalendar(year=2080, month=1)
   print(f"First week of 2080 Baishakh: {matrix[0]}")
   # >> First week of 2080 Baishakh: [0, 0, 0, 0, 0, 1, 2]  (Note: Weeks start on Sunday)

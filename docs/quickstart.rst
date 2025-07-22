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
   # >> Formatted in Nepali: बुधवार, भदौ १६, २०८१ साल, १०:३० पहिले

   # --- Arithmetic ---

   # Perform arithmetic between two fixed dates
   start_date = date(2081, 12, 1) # Chaitra 1, 2081
   end_of_year = date(2081, 12, 30) # End of Chaitra
   days_left = end_of_year - start_date
   print(f"Days from {start_date} to {end_of_year}: {days_left.days}")
   # >> Days from 2081-12-01 to 2081-12-30: 29

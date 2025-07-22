.. _user_guide_conversion:

Converting Between AD and BS
============================

A key feature of the ``bikram-sambat`` library is the ability to seamlessly convert between the Gregorian (AD) and Bikram Sambat (BS) calendar systems.

Converting from Bikram Sambat to Gregorian
------------------------------------------

To convert a ``date`` or ``datetime`` object from Bikram Sambat to Gregorian, use the ``togregorian`` method.

**Date Conversion**

.. code-block:: python

   from bikram_sambat import date

   # Create a BS date
   bs_date = date(2081, 1, 1)
   print(f"Bikram Sambat Date: {bs_date}")
   # >> Bikram Sambat Date: 2081-01-01

   # Convert to Gregorian
   ad_date = bs_date.togregorian()
   print(f"Gregorian (AD) Date: {ad_date}")
   # >> Gregorian (AD) Date: 2024-04-13

**Datetime Conversion**

.. code-block:: python

   from bikram_sambat import datetime, tz

   # Create a BS datetime in Nepal
   bs_dt = datetime(2081, 1, 1, 12, 0, 0, tzinfo=tz.nepal)
   print(f"Bikram Sambat Datetime: {bs_dt}")
   # >> Bikram Sambat Datetime: 2081-01-01T12:00:00+0545

   # Convert to Gregorian
   ad_dt = bs_dt.togregorian()
   print(f"Gregorian (AD) Datetime: {ad_dt}")
   # >> Gregorian (AD) Datetime: 2024-04-13 12:00:00+05:45

Converting from Gregorian to Bikram Sambat
------------------------------------------

To convert a date or datetime from Gregorian to Bikram Sambat, use the ``fromgregorian`` class method.

**Date Conversion**

.. code-block:: python

   from bikram_sambat import date
   from datetime import date as ad_date

   # Create a Gregorian date
   gregorian_date = ad_date(2024, 4, 13)
   print(f"Gregorian (AD) Date: {gregorian_date}")
   # >> Gregorian (AD) Date: 2024-04-13

   # Convert to Bikram Sambat
   bikram_sambat_date = date.fromgregorian(gregorian_date)
   print(f"Bikram Sambat Date: {bikram_sambat_date}")
   # >> Bikram Sambat Date: 2081-01-01

**Datetime Conversion**

.. code-block:: python

   from bikram_sambat import datetime
   from datetime import datetime as ad_datetime
   import pytz

   # Create a Gregorian datetime
   gregorian_dt = ad_datetime(2024, 4, 13, 12, 0, 0, tzinfo=pytz.utc)
   print(f"Gregorian (AD) Datetime: {gregorian_dt}")
   # >> Gregorian (AD) Datetime: 2024-04-13 12:00:00+00:00

   # Convert to Bikram Sambat
   bikram_sambat_dt = datetime.fromgregorian(gregorian_dt)
   print(f"Bikram Sambat Datetime: {bikram_sambat_dt}")
   # >> Bikram Sambat Datetime: 2081-01-01T12:00:00+0000

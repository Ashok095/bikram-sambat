.. _user_guide_conversion:

Converting Between AD and BS
============================

A key feature of the ``bikram-sambat`` library is the ability to seamlessly convert between the Gregorian (AD) and Bikram Sambat (BS) calendar systems.

Converting from Bikram Sambat to Gregorian
------------------------------------------

To convert a ``date`` or ``datetime`` object from Bikram Sambat to Gregorian, use the ``to_gregorian`` method.

**Date Conversion**

.. code-block:: python

   from bikram_sambat import date

   # Create a BS date
   bs_date = date(2081, 1, 1)
   print(f"Bikram Sambat Date: {bs_date}")

   # Convert to Gregorian
   ad_date = bs_date.to_gregorian()
   print(f"Gregorian (AD) Date: {ad_date}")

**Datetime Conversion**

.. code-block:: python

   from bikram_sambat import datetime, tz

   # Create a BS datetime in Nepal
   bs_dt = datetime(2081, 1, 1, 12, 0, 0, tzinfo=tz.nepal)
   print(f"Bikram Sambat Datetime: {bs_dt}")

   # Convert to Gregorian
   ad_dt = bs_dt.to_gregorian()
   print(f"Gregorian (AD) Datetime: {ad_dt}")

Converting from Gregorian to Bikram Sambat
------------------------------------------

To convert a date or datetime from Gregorian to Bikram Sambat, use the ``from_gregorian`` class method.

**Date Conversion**

.. code-block:: python

   from bikram_sambat import date
   from datetime import date as ad_date

   # Create a Gregorian date
   gregorian_date = ad_date(2024, 4, 13)
   print(f"Gregorian (AD) Date: {gregorian_date}")

   # Convert to Bikram Sambat
   bikram_sambat_date = date.from_gregorian(gregorian_date)
   print(f"Bikram Sambat Date: {bikram_sambat_date}")

**Datetime Conversion**

.. code-block:: python

   from bikram_sambat import datetime
   from datetime import datetime as ad_datetime
   import pytz

   # Create a Gregorian datetime
   gregorian_dt = ad_datetime(2024, 4, 13, 12, 0, 0, tzinfo=pytz.utc)
   print(f"Gregorian (AD) Datetime: {gregorian_dt}")

   # Convert to Bikram Sambat
   bikram_sambat_dt = datetime.from_gregorian(gregorian_dt)
   print(f"Bikram Sambat Datetime: {bikram_sambat_dt}")

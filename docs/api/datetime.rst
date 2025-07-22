.. _api_datetime:

``datetime``
============

.. automodule:: bikram_sambat.bs_datetime
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

   .. rubric:: Examples

   .. code-block:: python

      from bikram_sambat import datetime, timedelta, tz

      # Create a datetime
      dt = datetime(2081, 1, 1, 10, 30, 45)

      # Get the current datetime
      now = datetime.now()
      now_aware = datetime.now(tz.nepal)

      # Convert from Gregorian
      from datetime import datetime as ad_datetime
      ad_dt = ad_datetime(2024, 4, 13, 10, 30, 45)
      bs_dt = datetime.fromgregorian(ad_dt)

      # Convert to Gregorian
      ad_dt_new = bs_dt.togregorian()

      # Arithmetic
      dt2 = dt + timedelta(days=10, hours=5)
      diff = dt2 - dt

      # Timezones
      dt_utc = now_aware.astimezone(tz.utc)

      # Formatting
      print(dt.strftime("%Y-%m-%d %H:%M:%S"))
      # >> 2081-01-01 10:30:45

      print(dt_aware.strftime("%A, %B %d, %Y %I:%M:%S %p %Z"))
      # >> Saturday, Baishakh 01, 2081 10:00:00 AM Asia/Kathmandu

      print(dt_aware.strftime("%G, %N %D, %K %i:%l:%s %P"))
      # >> शनिबार, वैशाख ०१, २०८१ १०:००:०० पहिले
.. _api_date:

``date``
========

.. automodule:: bikram_sambat.bs_date
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

   .. note::
      **The ``isoweekday()`` paradox:** 
      In the standard Python ``datetime.date`` library, ``isoweekday()`` adheres strictly to the ISO-8601 standard, where Monday = 1 and Sunday = 7. 
      However, the Nepali calendar dictates that the week begins on Sunday. Therefore, in this library, ``weekday()`` correctly returns 0 for Sunday to align with Nepali conventions. 
      To maintain compatibility with some existing systems, ``isoweekday()`` simply returns ``weekday() + 1``, which results in **Sunday = 1**. This is technically a violation of the ISO-8601 standard, but is required for backward compatibility within this specific package structure.
      
      Developers should be aware of this difference when integrating with international systems!

   .. rubric:: Examples

   .. code-block:: python

      from bikram_sambat import date, timedelta

      # Create a date
      d = date(2081, 1, 1)

      # Get today's date
      today = date.today()

      # Convert from Gregorian
      from datetime import date as ad_date
      ad = ad_date(2024, 4, 13)
      bs = date.fromgregorian(ad)

      # Convert to Gregorian
      ad_new = bs.togregorian()

      # Arithmetic
      d2 = d + timedelta(days=10)
      diff = d2 - d

      # Formatting
      print(d.strftime("%Y-%m-%d"))
      # >> 2081-01-01

      print(d.strftime("%A, %B %d, %Y"))
      # >> Saturday, Baishakh 01, 2081

      print(d.strftime("%G, %N %D, %K"))
      # >> शनिबार, वैशाख ०१, २०८१
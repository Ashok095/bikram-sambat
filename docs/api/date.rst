.. _api_date:

``date``
========

.. automodule:: bikram_sambat.bs_date
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

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
      bs = date.from_gregorian(ad)

      # Convert to Gregorian
      ad_new = bs.to_gregorian()

      # Arithmetic
      d2 = d + timedelta(days=10)
      diff = d2 - d

      # Formatting
      print(d.strftime("%Y-%m-%d"))
      print(d.strftime("%A, %B %d, %Y"))
      print(d.strftime("%G, %N %D, %K"))

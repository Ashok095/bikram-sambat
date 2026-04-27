.. _api_calendar:

``calendar``
============

.. automodule:: bikram_sambat.calendar
   :members:
   :undoc-members:
   :show-inheritance:

   .. rubric:: Examples

   .. code-block:: python

      from bikram_sambat import bs_calendar, monthcalendar

      # Generate day-by-day mapping of BS month to AD dates
      bs_cal = bs_calendar(year=2080, month=1)
      print(bs_cal.days[0].ad_full_date)
      # >> 2023-04-14

      # Convert the generated calendar datamodels directly to a Python dictionary
      cal_dict = bs_cal.to_dict()
      print(cal_dict["bs_year"])
      # >> 2080

      # Create a UI-friendly week-by-week matrix (Starting on Sunday)
      matrix = monthcalendar(year=2080, month=1)
      print(matrix[0])
      # >> [0, 0, 0, 0, 0, 1, 2]

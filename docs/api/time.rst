.. _api_time:

``time``
========

.. automodule:: bikram_sambat.bs_time
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

   .. rubric:: Examples

   .. code-block:: python

      from bikram_sambat import time, tz

      # Create a time
      t = time(10, 30, 45)

      # Create a timezone-aware time
      t_aware = time(10, 30, 45, tzinfo=tz.nepal)

      # Formatting
      print(t.strftime("%H:%M:%S"))
      print(t_aware.strftime("%I:%M:%S %p %Z"))
      print(t_aware.strftime("%i:%l:%s %P"))

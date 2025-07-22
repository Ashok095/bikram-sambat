# Bikram Sambat (बि.सं.) for Python

[![PyPI Version](https://img.shields.io/pypi/v/bikram-sambat)](https://pypi.org/project/bikram-sambat)
[![Python Versions](https://img.shields.io/pypi/pyversions/bikram-sambat)](https://pypi.org/project/bikram-sambat)
[![CI/CD Status](https://github.com/Ashok095/bikram-sambat/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Ashok095/bikram-sambat/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/Ashok095/bikram-sambat/badge.svg?branch=main)](https://coveralls.io/github/Ashok095/bikram-sambat?branch=main)
[![License](https://img.shields.io/pypi/l/bikram-sambat)](https://opensource.org/licenses/MIT)

**Bikram Sambat (BS)**, also known as Vikram Samvat, is a historical Hindu calendar system used in Nepal and several states in India. It is approximately 56.7 years ahead of the Gregorian (AD) calendar.

This Python library provides a comprehensive and easy-to-use interface for working with Bikram Sambat dates and times. It offers `date`, `time`, and `datetime` objects that are analogous to Python's built-in `datetime` module, but specifically tailored for the BS calendar system. Key features include accurate AD-BS conversions, timezone awareness, BS-specific formatting (including Nepali numerals and month/weekday names), and robust parsing capabilities.

## 🛠️ Installation

Install the `bikram-sambat` package using pip:

```bash
pip install bikram-sambat
```

**Requirements**:

- Python 3.8 or higher
- The pytz library (automatically installed as a dependency)

## ✨ Features

- **BS-Specific Date, Time, and DateTime Objects:**
  - `bikram_sambat.date`: Represents a Bikram Sambat date (year, month, day).
  - `bikram_sambat.time`: Represents a Bikram Sambat time (hour, minute, second, microsecond), with timezone support.
  - `bikram_sambat.datetime`: Represents a Bikram Sambat date and time, with timezone support.
- **Accurate AD ⇔ BS Conversions:**
  - Reliably convert between Gregorian (AD) and Bikram Sambat (BS) dates and datetimes.
  - Handles the complex mapping of days between the two calendar systems.
- **Comprehensive Formatting (`strftime`):**
  - Format dates and times into custom string representations.
  - Supports standard `strftime` directives.
  - Includes BS-specific directives for:
    - Nepali numerals (e.g., `२०८१` for year, `१५` for day).
    - Full and abbreviated month names in English (e.g., "Baishakh", "Bai").
    - Full and abbreviated month names in Nepali (e.g., "वैशाख").
    - Full and abbreviated weekday names in English and Nepali.
- **Robust Parsing (`fromstrftime`):**
  - Parse BS date/time strings from various formats into corresponding objects.
  - Handles Nepali numerals and month/weekday names in input strings.
- **Timezone Awareness:**
  - Full support for timezone-aware `time` and `datetime` objects using `pytz`.
  - Easy access to common timezones like Nepal Standard Time (`Asia/Kathmandu`) and UTC.
  - Convert BS datetimes between different timezones.
- **Arithmetic Operations:**
  - Perform addition and subtraction with `timedelta` objects.
  - Calculate differences between BS dates/datetimes.
- **Standard Python Interface:**
  - Familiar API, largely compatible with Python's built-in `datetime` module, making it easy to learn and use.
  - Inherits from `datetime.date`, `datetime.time`, and `datetime.datetime` where appropriate.
- **Nepali Calendar Data:**
  - Includes data for BS calendar month lengths for a wide range of years (typically 1901 BS to 2199 BS).
- **Bikram Sambat Calendar Data:**
  - Includes pre-compiled data for Bikram Sambat month lengths for a wide range of years (currently 1901 BS to 2199 BS).
  - _Disclaimer: The calendar data (days in each BS month) is based on aggregated information from various public sources and existing calendar implementations. See the "Calendar Data and Accuracy" section for more details._

---

## 📅 Calendar Data and Accuracy

The Bikram Sambat calendar is a lunisolar calendar, and the exact number of days in each month can vary from year to year. This library relies on pre-compiled data for the number of days in each Bikram Sambat month across a range of years (currently 1901 BS to 2199 BS).

This data has been aggregated and cross-referenced from several publicly available sources and existing calendar implementations, including:

1.  [NepDate by TheCrossLegCoder (C#)](https://github.com/TheCrossLegCoder/NepDate/blob/main/src/NepDate/Core/Dictionaries/NepaliToEnglish.cs)
2.  [nepali-datetime by amitgaru2 (Python)](https://github.com/amitgaru2/nepali-datetime/tree/master/nepali_datetime/data)
3.  Traditional Nepali calendar software.

While efforts have been made to ensure accuracy, discrepancies can exist between different calendar sources for certain years or months due to the traditional methods of BS calendar determination. The conversions and date operations within this library are accurate based on the embedded calendar data. For official or legal purposes, please consult an officially published Nepali calendar (Patro).

## 🚀 Quick Start

Here's a quick glimpse of how to use `bikram-sambat`:

```python
from bikram_sambat import date, time, datetime, timedelta
from bikram_sambat.timezone import nepal, utc

# --- Bikram Sambat Dates ---
# Create a BS date
bs_date = date(2080, 5, 15)  # BS: 2080 Bhadra 15
print(f"BS Date: {bs_date}")
# >> BS Date: 2080-05-15

print(f"Year: {bs_date.year}, Month: {bs_date.month}, Day: {bs_date.day}")
# >> Year: 2080, Month: 5, Day: 15

# Today's BS date
today_bs = date.today()
print(f"Today (BS): {today_bs}")
# >> Today (BS): 2082-04-06

# Convert BS to AD
ad_date = bs_date.togregorian()
print(f"Equivalent AD Date: {ad_date}")
# >> Equivalent AD Date: 2023-09-01

# Convert AD to BS
from datetime import date as ad_py_date
ad_another_date = ad_py_date(2024, 1, 1)
bs_converted_date = date.fromgregorian(ad_another_date)
print(f"AD {ad_another_date} is BS {bs_converted_date}")
# >> AD 2024-01-01 is BS 2080-09-16

# Formatting
print(bs_date.strftime("%Y %B %d, %A (%K %N %D, %G)"))
# >> 2080 Bhadra 15, Friday (२०८० भदौ १५, शुक्रबार)

# --- Bikram Sambat Times ---
# Create a BS time (naive)
bs_time = time(14, 30, 45)
print(f"BS Time: {bs_time}")
# >> BS Time: 14:30:45


# Create a timezone-aware BS time
bs_time_nepal = time(10, 15, 0, tzinfo=nepal)
print(f"BS Time (Nepal): {bs_time_nepal} {bs_time_nepal}")
# >> BS Time (Nepal): 10:15:00 10:15:00


# Formatting time
print(bs_time_nepal.strftime("%I:%M:%S %p %P [%Z]"))
# >> 10:15:00 AM पहिले [Asia/Kathmandu]


# --- Bikram Sambat Datetimes ---
# Create a naive BS datetime
bs_dt_naive = datetime(2081, 1, 1, 10, 0, 0) # BS: 2081 Baishakh 1, 10:00 AM
print(f"BS Datetime (naive): {bs_dt_naive}")
# >> BS Datetime (naive): 2081-01-01T10:00:00


# Create a timezone-aware BS datetime
bs_dt_aware = datetime(2081, 1, 1, 10, 0, 0, tzinfo=nepal)
print(f"BS Datetime (aware): {bs_dt_aware}")
# >> BS Datetime (aware): 2081-01-01T10:00:00+0545


# Current BS datetime (naive)
now_bs_naive = datetime.now()
print(f"Now (BS, naive): {now_bs_naive}")
# >> Now (BS, naive): 2082-04-06T03:41:28.962229


# Current BS datetime in a specific timezone
now_bs_nepal = datetime.now(nepal)
print(f"Now (BS, Nepal): {now_bs_nepal}")
# >> Now (BS, Nepal): 2082-04-06T09:26:28.962327+0545


# Convert to another timezone
now_bs_utc = now_bs_nepal.astimezone(utc)
print(f"Now (BS, UTC): {now_bs_utc}")
# >> Now (BS, UTC): 2082-04-06T03:41:28.962327+0000


# Convert BS datetime to AD datetime
ad_dt = bs_dt_aware.togregorian()
print(f"Equivalent AD Datetime: {ad_dt}")
# >> Equivalent AD Datetime: 2024-04-13 10:00:00+05:45

# --- Arithmetic ---
delta = timedelta(days=10, hours=5)
future_dt = now_bs_nepal + delta
print(f"10 days, 5 hours from now (BS): {future_dt}")
# >> 10 days, 5 hours from now (BS): 2082-04-16T14:26:28.962327+0545


diff = future_dt - now_bs_nepal
print(f"Difference: {diff}")
# >> Difference: 10 days, 5:00:00


```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](https://mit-license.org/) file for details.

## 🤝 Contributing

Contributions are welcome!.

## 📚 Full Documentation

Read the full documentattion here: https://bikram-sambat.readthedocs.io/en/latest/

## 🙌 Support

If you find this project useful, consider starring ⭐ the repo or sharing it.
For feature requests or issues, please open a ticket at the [Issue Tracker](https://github.com/ashok095/bikram-sambat/issues)

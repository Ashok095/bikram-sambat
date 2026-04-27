# Bikram Sambat - Developer Cheatsheet & Architecture

This document provides a quick overview of the core capabilities, API surfaces, and internal patterns of the `bikram-sambat` Python library. It is designed to help developers and contributors quickly understand and integrate the library.

## Core Capabilities
`bikram-sambat` is a drop-in replacement/extension for Python's standard `datetime` module, specifically tailored for the Bikram Sambat (BS) / Nepali calendar. 

- **Range Supported**: 1901 BS to 2199 BS.
- **Key Modules**: `date`, `time`, `datetime`, `timedelta`, `tz` (timezone), `bs_calendar`, `ad_calendar`, `monthcalendar`.
- **Inheritance**: `BSDate` inherits from `datetime.date`. `BSDatetime` inherits from `datetime.datetime`.

## Key Architectural Decisions
1. **Zero-indexing for Weekdays**: Unlike Python's `datetime` which uses Monday=0, `bikram-sambat` strictly uses **Sunday=0** (Aaitabar) and Saturday=6 (Sanibar). This applies to `.weekday()` methods and the `monthcalendar` matrix.
2. **Nepali Number & Text Support**: `strftime` and `fromstrftime` support Nepali digits (०-९) and Devanagari text using specific format directives.
3. **Immutability**: All date/time objects are immutable, behaving exactly like standard Python `datetime` objects.

## Comprehensive API Reference

This section details every class, attribute, and method available via `from bikram_sambat import ...`.

### 1. `BSDate` (`date`)
**Inherits from `datetime.date`. Immutable BS Date.**
- **Attributes:** `year`, `month`, `day`
- **Class Methods:**
  - `BSDate.today()`: Returns current local BS date.
  - `BSDate.fromgregorian(greg_date_input)`: Converts standard `datetime.date` to `BSDate`.
  - `BSDate.fromisoformat(date_string)`: Parses string in 'YYYY-MM-DD' format.
  - `BSDate.fromstrftime(date_string, format)`: Parses formatted strings (supports English/Nepali texts).
  - `BSDate.bs_fromordinal(ordinal)`: Converts BS ordinal integer to `BSDate`.
- **Instance Methods:**
  - `togregorian()`: Returns standard `datetime.date`.
  - `replace(year=-1, month=-1, day=-1)`: Returns a modified `BSDate`.
  - `weekday()`: Returns integer **(Sunday=0, Saturday=6)**.
  - `isoweekday()`: Returns integer **(Sunday=1, Saturday=7)**.
  - `strftime(format)`: Formats date with standard and custom BS directives.
  - `isoformat()`: Returns 'YYYY-MM-DD'.
  - `ctime()`: Returns ctime-style string.
  - `bs_toordinal()`: Returns integer BS ordinal.
- **Operations:** Supports `+` / `-` with `timedelta`, and `-` with another `BSDate`.

### 2. `BSTime` (`time`)
**Inherits from `datetime.time`. Immutable BS Time.**
- **Attributes:** `hour`, `minute`, `second`, `microsecond`, `tzinfo`
- **Class Methods:**
  - `BSTime.now(tz=None)`: Returns current time, optionally in a timezone.
  - `BSTime.fromisoformat(time_string)`: Parses 'HH:MM:SS' format.
  - `BSTime.fromstrftime(time_string, format)`: Parses formatted time string.
- **Instance Methods:**
  - `replace(hour=-1, minute=-1, second=-1, microsecond=-1, tzinfo=True)`: Returns modified `BSTime`.
  - `isoformat(timespec='auto')`: Returns ISO 8601 string.
  - `strftime(format)`: Formats time.

### 3. `BSDatetime` (`datetime`)
**Inherits from `datetime.datetime`. Immutable BS Datetime.**
- **Attributes:** `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`, `tzinfo`
- **Class Methods:**
  - `BSDatetime.now(tz=None)`: Returns current local or timezone-aware BS datetime.
  - `BSDatetime.today()`: Returns current local BS datetime.
  - `BSDatetime.utcnow()`: Returns current UTC BS datetime.
  - `BSDatetime.fromgregorian(greg_dt)`: Converts standard `datetime.datetime` to `BSDatetime`.
  - `BSDatetime.fromtimestamp(timestamp, tz=None)`: Converts POSIX timestamp to `BSDatetime`.
  - `BSDatetime.utcfromtimestamp(timestamp)`: Converts POSIX timestamp to UTC `BSDatetime`.
  - `BSDatetime.fromisoformat(date_string)`: Parses ISO 8601 string.
  - `BSDatetime.fromstrftime(date_string, format)`: Parses string via format.
- **Instance Methods:**
  - `togregorian()`: Returns standard `datetime.datetime`.
  - `date()`: Returns `BSDate` object.
  - `time()`: Returns `BSTime` (naive).
  - `timetz()`: Returns `BSTime` (aware).
  - `replace(...)`: Returns modified `BSDatetime`.
  - `astimezone(tz=None)`: Converts to a different timezone.
  - `timestamp()`: Returns POSIX timestamp.
  - `weekday()`: Returns integer **(Sunday=0, Saturday=6)**.
  - `isoweekday()`: Returns integer **(Sunday=1, Saturday=7)**.
  - `strftime(format)`: Formats datetime.
  - `isoformat(sep='T', timespec='auto')`: Returns ISO string.
  - `ctime()`: Returns ctime-style string.
- **Operations:** Supports `+` / `-` with `timedelta`, and `-` with another `BSDatetime`.

### 4. `BSTimedelta` (`timedelta`)
**Inherits from `datetime.timedelta`.**
- **Attributes:** `days`, `seconds`, `microseconds`
- **Methods:** `total_seconds()`: Returns total duration in seconds.

### 5. Timezones (`tz` module)
Wrappers and configurations utilizing `pytz`.
- `tz.nepal`: Pre-configured Nepal Standard Time (`+05:45`).
- `tz.utc`: Coordinated Universal Time (`+00:00`).
- `tz.india`: India Standard Time (`+05:30`).
- `tz.get_timezone(name)`: Retrieves timezone by TZ database name.
- `tz.all_timezones_list()`: Returns list of supported timezone names.

### 6. Calendar Module (`calendar.py`)
Provides structural mappings and matrices. All functions are `@functools.lru_cache` optimized.
- `bs_calendar(year, month=None)`: Returns `CalendarMonthData` mapped from BS Day 1. (If `month` omitted, returns `List[CalendarMonthData]` for the whole year).
- `ad_calendar(year, month=None)`: Returns `CalendarMonthData` mapped from AD Day 1.
- `monthcalendar(year, month)`: Returns a week-by-week matrix (`List[List[int]]`) of the given BS month, starting on **Sunday**.
- **Data Models:** Both `CalendarMonthData` and `CalendarDayData` expose a `.to_dict()` method for easy JSON serialization.

### 7. Formatting Directives (`strftime` / `fromstrftime`)
In addition to standard directives, BS classes support:
- `%K`: Year with century in Nepali (e.g., २०८१)
- `%N`: Full month name in Nepali (e.g., वैशाख)
- `%D`: Day of month in Nepali (e.g., १५)
- `%G`: Full weekday name in Nepali (e.g., आइतबार)
- `%P`: AM/PM in Nepali (पूर्वाह्न / अपराह्न)

## Integration Best Practices
- When writing code that interfaces with both standard Python `datetime` and `bikram-sambat`, aggressively alias `datetime` to `py_dt` to avoid namespace collisions.
- Use the `.togregorian()` and `.fromgregorian()` class methods over manual tuple destructuring for cross-calendar math.
- For UI components requiring calendars, heavily leverage `bs_calendar` and `monthcalendar` as they are heavily cached (`functools.lru_cache`) and optimized for rapid execution.
- Remember the `weekday()` offset: Python AD calendars expect `0=Monday`. BS calendars in this package expect `0=Sunday`. Adjust rendering logic accordingly!

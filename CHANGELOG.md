# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-04-27

### Added
- **Calendar Generation Module**: Introduced `bikram_sambat.calendar` module for fetching full day-by-day mapping of BS and AD dates.
- **Calendar Models**: Added `CalendarMonthData` and `CalendarDayData` dataclasses.
- **`to_dict()` Support**: Added `.to_dict()` methods on calendar models for easy JSON serialization.
- **Matrix Generation**: Added `monthcalendar(year, month)` to generate a UI-friendly week-by-week calendar matrix (starting on Sunday).
- **Developer Cheatsheet**: Added an extensive `CHEATSHEET.md` mapping out the entire API architecture.
- **Sphinx Documentation**: Added new `docs/api/calendar.rst` for the new calendar tools and updated `docs/quickstart.rst`.

### Changed
- **`isoweekday` Documentation**: Added explicit Sphinx documentation explaining why `isoweekday()` returns 1 for Sunday (to align with the package's internal Nepali week indexing vs the ISO-8601 standard).
- **`replace()` Sentinel Values**: Updated `BSDate.replace()` to use Pythonic `Optional[SupportsIndex] = None` instead of `-1`.

### Fixed
- **`BSDatetime.to_datetime()`**: Fixed a major `pytz` anti-pattern by safely returning the localized datetime object, preventing potential daylight-saving time edge-case bugs.
- **AM/PM Constants**: Ensured standard `पूर्वाह्न` and `अपराह्न` terminology across `README.md` and standard format variables.

## [0.1.1] - 2023-09-02
### Added
- Initial core release including `date`, `time`, `datetime`, and timezone extensions for the Bikram Sambat calendar.

import pytest
from bikram_sambat.calendar import bs_calendar, ad_calendar, monthcalendar, CalendarMonthData, CalendarDayData

def test_bs_calendar_month():
    # Fetch BS Calendar for 2080-01 (Baishakh)
    # Baishakh 2080 has 31 days
    data = bs_calendar(year=2080, month=1)
    
    assert isinstance(data, CalendarMonthData)
    assert data.bs_year == 2080
    assert data.bs_month == 1
    assert data.ad_year == 2023
    assert data.ad_month == 4  # Baishakh starts mid-April
    assert len(data.days) == 31
    
    first_day = data.days[0]
    assert first_day.bs_year == 2080
    assert first_day.bs_month == 1
    assert first_day.bs_day == 1
    assert first_day.ad_year == 2023
    assert first_day.ad_month == 4
    assert first_day.ad_day == 14
    assert first_day.ad_full_date == "2023-04-14"
    assert first_day.week_day == 5  # 0=Sun, 5=Friday

def test_bs_calendar_custom_data():
    # User provided cases
    # 2083-01-01 -> 2026-04-14
    data1 = bs_calendar(2083, 1)
    day1 = data1.days[0]
    assert day1.bs_year == 2083
    assert day1.bs_month == 1
    assert day1.bs_day == 1
    assert day1.ad_day == 14
    assert day1.ad_full_date == "2026-04-14"

    # 2082-11-01 -> 2026-02-13
    data2 = bs_calendar(2082, 11)
    day2 = data2.days[0]
    assert day2.bs_year == 2082
    assert day2.bs_month == 11
    assert day2.bs_day == 1
    assert day2.ad_day == 13
    assert day2.ad_full_date == "2026-02-13"
    assert day2.week_day == 5

    # 2082-12-01 -> 2026-03-15
    data3 = bs_calendar(2082, 12)
    day3 = data3.days[0]
    assert day3.bs_year == 2082
    assert day3.bs_month == 12
    assert day3.bs_day == 1
    assert day3.ad_day == 15
    assert day3.ad_full_date == "2026-03-15"
    assert day3.week_day == 0

    # 2079-12-01 -> 2023-03-15
    data4 = bs_calendar(2079, 12)
    day4 = data4.days[0]
    assert day4.bs_year == 2079
    assert day4.bs_month == 12
    assert day4.bs_day == 1
    assert day4.ad_day == 15
    assert day4.ad_full_date == "2023-03-15"
    assert day4.week_day == 3

def test_bs_calendar_year():
    # Fetch full BS year 2080
    year_data = bs_calendar(year=2080)
    
    assert isinstance(year_data, list)
    assert len(year_data) == 12
    assert all(isinstance(m, CalendarMonthData) for m in year_data)
    assert year_data[0].bs_month == 1
    assert year_data[11].bs_month == 12

def test_ad_calendar_month():
    # Fetch AD Calendar for 2024-02 (Leap year)
    data = ad_calendar(year=2024, month=2)
    
    assert isinstance(data, CalendarMonthData)
    assert data.ad_year == 2024
    assert data.ad_month == 2
    assert data.bs_year == 2080
    assert data.bs_month == 10 # Feb starts in Magh
    assert len(data.days) == 29
    
    first_day = data.days[0]
    assert first_day.ad_year == 2024
    assert first_day.ad_month == 2
    assert first_day.ad_day == 1
    assert first_day.bs_year == 2080
    assert first_day.bs_month == 10
    assert first_day.bs_day == 18
    assert first_day.ad_full_date == "2024-02-01"
    assert first_day.week_day == 4  # 0=Sun, 4=Thursday

def test_ad_calendar_year():
    # Fetch full AD year 2024
    year_data = ad_calendar(year=2024)
    
    assert isinstance(year_data, list)
    assert len(year_data) == 12
    assert all(isinstance(m, CalendarMonthData) for m in year_data)
    assert year_data[0].ad_month == 1
    assert year_data[11].ad_month == 12

def test_monthcalendar():
    # 2080 Baishakh has 31 days, starts on Friday (5)
    matrix = monthcalendar(year=2080, month=1)
    
    # Check first week
    assert matrix[0] == [0, 0, 0, 0, 0, 1, 2]
    # Check intermediate week
    assert matrix[1] == [3, 4, 5, 6, 7, 8, 9]
    # Check total length
    assert len(matrix) == 6
    # Check last week (ends on Sunday, so pads to Saturday)
    assert matrix[5] == [31, 0, 0, 0, 0, 0, 0]

def test_monthcalendar_starts_sunday():
    # 2081 Baishakh 1 is on Saturday (6)
    matrix = monthcalendar(year=2081, month=1)
    assert matrix[0] == [0, 0, 0, 0, 0, 0, 1]
    
    # 2081 Jestha 1 is on Tuesday (2)
    matrix = monthcalendar(year=2081, month=2)
    assert matrix[0] == [0, 0, 1, 2, 3, 4, 5]

def test_invalid_bs_calendar_input():
    with pytest.raises(ValueError):
        bs_calendar(year=1800)
    with pytest.raises(ValueError):
        bs_calendar(year=2080, month=13)

def test_invalid_ad_calendar_input():
    with pytest.raises(ValueError):
        ad_calendar(year=2024, month=13)

def test_invalid_monthcalendar_input():
    with pytest.raises(ValueError):
        monthcalendar(year=1800, month=1)
    with pytest.raises(ValueError):
        monthcalendar(year=2080, month=13)

def test_to_dict():
    # Test to_dict on CalendarMonthData and CalendarDayData
    data = bs_calendar(year=2083, month=1)
    
    # Should convert CalendarMonthData to a dict
    month_dict = data.to_dict()
    assert isinstance(month_dict, dict)
    assert month_dict["bs_year"] == 2083
    assert month_dict["bs_month"] == 1
    
    # Nested CalendarDayData should be a list of dicts
    assert isinstance(month_dict["days"], list)
    assert isinstance(month_dict["days"][0], dict)
    assert month_dict["days"][0]["bs_year"] == 2083
    assert month_dict["days"][0]["bs_month"] == 1
    assert month_dict["days"][0]["bs_day"] == 1
    assert month_dict["days"][0]["ad_full_date"] == "2026-04-14"

"""Provides a calendar system for Bikram Sambat (BS) dates.

This module offers functions to generate calendar data structures, providing
day-by-day mapping between BS and AD dates. It includes methods to fetch
data for specific months or entire years, and a `monthcalendar` function
similar to the standard Python `calendar` module.
"""

from dataclasses import dataclass
from typing import List, Optional, Union
import functools
import calendar as pycalendar
import datetime

from .bs_date import BSDate
from .conversion import ad_to_bs, bs_to_ad
from .data.calendar_data import YEAR_MONTH_DAYS_BS
from . import config

@dataclass
class CalendarDayData:
    """Represents a single day in the calendar with both BS and AD dates."""
    bs_year: int
    bs_month: int
    bs_day: int
    ad_year: int
    ad_month: int
    ad_day: int
    weekday: int  # 0=Sunday, 6=Saturday

@dataclass
class CalendarMonthData:
    """Represents a month in the calendar."""
    bs_year: int
    bs_month: int
    ad_year: int
    ad_month: int
    days: List[CalendarDayData]

@functools.lru_cache(maxsize=128)
def bs_calendar(year: int, month: Optional[int] = None) -> Union[CalendarMonthData, List[CalendarMonthData]]:
    """Generates calendar data for a given BS year and optional month.
    
    If `month` is provided, returns data for that specific BS month.
    If `month` is None, returns a list of data for all 12 BS months.
    """
    if month is None:
        return [bs_calendar(year, m) for m in range(1, 13)] # type: ignore
        
    if not (config.BS_MIN_SUPPORTED_YEAR <= year <= config.BS_MAX_SUPPORTED_YEAR):
        raise ValueError(f"Year {year} is out of the supported range.")
    if not (1 <= month <= 12):
        raise ValueError(f"Month {month} must be between 1 and 12.")
        
    days_in_month = YEAR_MONTH_DAYS_BS[year][month - 1]
    days_data = []
    
    first_day_ad = bs_to_ad(year, month, 1)
    
    for day in range(1, days_in_month + 1):
        ad_date = bs_to_ad(year, month, day)
        # Using BSDate to calculate the weekday (0=Sun, 6=Sat)
        bs_date_obj = BSDate(year, month, day)
        
        days_data.append(CalendarDayData(
            bs_year=year,
            bs_month=month,
            bs_day=day,
            ad_year=ad_date.year,
            ad_month=ad_date.month,
            ad_day=ad_date.day,
            weekday=bs_date_obj.weekday()
        ))
        
    return CalendarMonthData(
        bs_year=year,
        bs_month=month,
        ad_year=first_day_ad.year,
        ad_month=first_day_ad.month,
        days=days_data
    )

@functools.lru_cache(maxsize=128)
def ad_calendar(year: int, month: Optional[int] = None) -> Union[CalendarMonthData, List[CalendarMonthData]]:
    """Generates calendar data for a given AD year and optional month.
    
    If `month` is provided, returns data for that specific AD month.
    If `month` is None, returns a list of data for all 12 AD months.
    """
    if month is None:
        return [ad_calendar(year, m) for m in range(1, 13)] # type: ignore
        
    if not (1 <= month <= 12):
        raise ValueError(f"Month {month} must be between 1 and 12.")
        
    _, days_in_month = pycalendar.monthrange(year, month)
    days_data = []
    
    # Calculate the BS date for the first day of the AD month
    first_day_ad = datetime.date(year, month, 1)
    first_bs_year, first_bs_month, _ = ad_to_bs(first_day_ad)
    
    for day in range(1, days_in_month + 1):
        ad_date = datetime.date(year, month, day)
        bs_y, bs_m, bs_d = ad_to_bs(ad_date)
        bs_date_obj = BSDate(bs_y, bs_m, bs_d)
        
        days_data.append(CalendarDayData(
            bs_year=bs_y,
            bs_month=bs_m,
            bs_day=bs_d,
            ad_year=year,
            ad_month=month,
            ad_day=day,
            weekday=bs_date_obj.weekday()
        ))
        
    return CalendarMonthData(
        bs_year=first_bs_year,
        bs_month=first_bs_month,
        ad_year=year,
        ad_month=month,
        days=days_data
    )

@functools.lru_cache(maxsize=128)
def monthcalendar(year: int, month: int) -> List[List[int]]:
    """Returns a matrix representing a BS month's calendar.
    
    Each row represents a week; days outside the month are represented by zeros.
    The week starts on Sunday.
    """
    if not (config.BS_MIN_SUPPORTED_YEAR <= year <= config.BS_MAX_SUPPORTED_YEAR):
        raise ValueError(f"Year {year} is out of the supported range.")
    if not (1 <= month <= 12):
        raise ValueError(f"Month {month} must be between 1 and 12.")
        
    days_in_month = YEAR_MONTH_DAYS_BS[year][month - 1]
    first_day = BSDate(year, month, 1)
    start_weekday = first_day.weekday() # 0 = Sunday
    
    matrix = []
    current_week = [0] * start_weekday
    
    for day in range(1, days_in_month + 1):
        current_week.append(day)
        if len(current_week) == 7:
            matrix.append(current_week)
            current_week = []
            
    if current_week:
        # Pad the last week with zeros
        current_week.extend([0] * (7 - len(current_week)))
        matrix.append(current_week)
        
    return matrix

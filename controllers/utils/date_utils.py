"""
date_utils.py

This module provides utility functions for handling date and time operations in the Restaurant Management System (RMS).
It includes functions for parsing, formatting, calculating differences between dates, and generating date-related reports.

📌 Features:
- Convert date strings to datetime objects and vice versa.
- Calculate the difference between two dates.
- Add or subtract days from a given date.
- Check if a given date is in the past, future, or today.
- Get weekday names, first and last days of a week.
- Retrieve the current date and time for use in the system.

🛠️ Dependencies:
- datetime: For handling date and time operations.
- calendar: For working with calendars and checking weekdays.

Functions:

1. parse_date(date_string: str, date_format: str = "%Y-%m-%d") -> datetime
    - Converts a date string into a datetime object based on the specified format.

2. format_date(date: datetime, date_format: str = "%Y-%m-%d") -> str
    - Converts a datetime object into a formatted date string according to the specified format.

3. get_days_difference(start_date: datetime, end_date: datetime) -> int
    - Calculates the difference in days between two given dates.

4. add_days_to_date(date: datetime, days: int) -> datetime
    - Adds a specific number of days to a given date.

5. subtract_days_from_date(date: datetime, days: int) -> datetime
    - Subtracts a specific number of days from a given date.

6. get_current_date() -> datetime
    - Retrieves the current date and time as a datetime object.

7. is_past_date(date: datetime) -> bool
    - Checks if a given date is in the past relative to the current date and time.

8. is_future_date(date: datetime) -> bool
    - Checks if a given date is in the future relative to the current date and time.

9. is_today(date: datetime) -> bool
    - Checks if a given date is today's date.

10. get_weekday_name(date: datetime) -> str
    - Returns the name of the weekday for a given date (e.g., "Monday", "Tuesday").

11. get_first_day_of_week(date: datetime) -> datetime
    - Returns the first day (Monday) of the week for a given date.

12. get_last_day_of_week(date: datetime) -> datetime
    - Returns the last day (Sunday) of the week for a given date.

"""

from datetime import datetime, timedelta
import calendar

def parse_date(date_string: str, date_format: str = "%Y-%m-%d") -> datetime:
    """
    Converts a date string into a datetime object.

    :param date_string: The date string to convert.
    :param date_format: The format of the date string (default: "%Y-%m-%d").
    :return: The corresponding datetime object.
    """
    return datetime.strptime(date_string, date_format)

def format_date(date: datetime, date_format: str = "%Y-%m-%d") -> str:
    """
    Converts a datetime object into a formatted date string.

    :param date: The datetime object to format.
    :param date_format: The desired date format (default: "%Y-%m-%d").
    :return: The formatted date string.
    """
    return date.strftime(date_format)

def get_days_difference(start_date: datetime, end_date: datetime) -> int:
    """
    Calculates the difference in days between two dates.

    :param start_date: The start date.
    :param end_date: The end date.
    :return: The number of days between the two dates.
    """
    return (end_date - start_date).days

def add_days_to_date(date: datetime, days: int) -> datetime:
    """
    Adds a specific number of days to a given date.

    :param date: The initial date.
    :param days: The number of days to add.
    :return: The new date after adding the specified number of days.
    """
    return date + timedelta(days=days)

def subtract_days_from_date(date: datetime, days: int) -> datetime:
    """
    Subtracts a specific number of days from a given date.

    :param date: The initial date.
    :param days: The number of days to subtract.
    :return: The new date after subtracting the specified number of days.
    """
    return date - timedelta(days=days)

def get_current_date() -> datetime:
    """
    Retrieves the current date and time.

    :return: The current datetime object.
    """
    return datetime.now()

def is_past_date(date: datetime) -> bool:
    """
    Checks if a given date is in the past.

    :param date: The date to check.
    :return: True if the date is in the past, False otherwise.
    """
    return date < datetime.now()

def is_future_date(date: datetime) -> bool:
    """
    Checks if a given date is in the future.

    :param date: The date to check.
    :return: True if the date is in the future, False otherwise.
    """
    return date > datetime.now()

def is_today(date: datetime) -> bool:
    """
    Checks if the given date is today.

    :param date: The date to check.
    :return: True if the date is today, False otherwise.
    """
    return date.date() == datetime.now().date()

def get_weekday_name(date: datetime) -> str:
    """
    Returns the name of the weekday for a given date.

    :param date: The date to check.
    :return: The name of the weekday (e.g., "Monday", "Tuesday").
    """
    return calendar.day_name[date.weekday()]

def get_first_day_of_week(date: datetime) -> datetime:
    """
    Returns the first day (Monday) of the week for a given date.

    :param date: The date to calculate the first day of the week for.
    :return: The datetime object of the first day of the week (Monday).
    """
    start_of_week = date - timedelta(days=date.weekday())
    return start_of_week

def get_last_day_of_week(date: datetime) -> datetime:
    """
    Returns the last day (Sunday) of the week for a given date.

    :param date: The date to calculate the last day of the week for.
    :return: The datetime object of the last day of the week (Sunday).
    """
    end_of_week = date + timedelta(days=(6 - date.weekday()))
    return end_of_week

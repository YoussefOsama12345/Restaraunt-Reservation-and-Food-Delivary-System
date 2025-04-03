"""
report_utils.py

This module provides utility functions for generating and formatting reports within the Restaurant Management System (RMS).
It includes functions for summarizing and processing data, calculating totals, and formatting report outputs.

📌 Features:
- Generate and format reports for various RMS sections (e.g., sales, reservations, attendance).
- Calculate totals, averages, and other aggregates.
- Format data for display or export (e.g., CSV, PDF).
- Handle date filtering and formatting for reports.

🛠️ Dependencies:
- datetime -> For handling date and time operations (e.g., date filtering).
- calendar -> For working with weekdays and calculating weekly summaries.
- csv -> For generating CSV reports.
- pandas (optional) -> For advanced data manipulation and aggregation.

Functions:
- `generate_sales_report(data: List[Dict], start_date: datetime, end_date: datetime) -> str`: Generates a formatted sales report for a specific date range.
- `generate_reservation_report(data: List[Dict], start_date: datetime, end_date: datetime) -> str`: Generates a formatted reservation report for a specific date range.
- `calculate_total_sales(data: List[Dict]) -> float`: Calculates the total sales amount from a list of sales data.
- `generate_daily_report(data: List[Dict], date: datetime) -> str`: Generates a daily sales report for a specific date.
- `filter_data_by_date(data: List[Dict], start_date: datetime, end_date: datetime) -> List[Dict]`: Filters data by a specified date range.
- `format_report_as_csv(data: List[Dict], filename: str) -> None`: Formats the report data as CSV and saves it to a file.

Note: This module is designed to be used in conjunction with specific data controllers, such as sales, reservations, and attendance controllers, to provide comprehensive reporting capabilities.
"""

import datetime
import csv

def generate_sales_report(data: list, start_date: datetime.date, end_date: datetime.date) -> str:
    """
    Generates a formatted sales report for a given date range.
    
    :param data: The sales data to process, usually in the form of a list of dictionaries.
    :param start_date: The start date for the report.
    :param end_date: The end date for the report.
    :return: A string containing the formatted sales report.
    """
    
    filtered_data = filter_data_by_date(data, start_date, end_date)
    total_sales = calculate_total_sales(filtered_data)
    report = f"Sales Report from {start_date} to {end_date}\n"
    report += f"Total Sales: ${total_sales}\n"
    
    return report


def filter_data_by_date(data: list, start_date: datetime.date, end_date: datetime.date) -> list:
    """
    Filters data within a specified date range.
    
    :param data: The data to filter, typically a list of dictionaries.
    :param start_date: The start date for filtering.
    :param end_date: The end date for filtering.
    :return: A list of filtered data.
    """
    return [entry for entry in data if start_date <= entry['date'] <= end_date]


def calculate_total_sales(data: list) -> float:
    """
    Calculates the total sales amount from the sales data.
    
    :param data: The sales data, typically a list of dictionaries containing sales information.
    :return: The total sales amount.
    """
    return sum(entry['amount'] for entry in data)


def format_report_as_csv(data: list, filename: str) -> None:
    """
    Formats the report data as CSV and saves it to a file.
    
    :param data: The data to convert into CSV format, typically a list of dictionaries.
    :param filename: The name of the file to save the CSV.
    :return: None
    """
    keys = data[0].keys()
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

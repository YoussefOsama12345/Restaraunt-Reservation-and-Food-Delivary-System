"""
file_utils.py

This module provides utility functions for managing files in the Restaurant Management System (RMS). 
It includes functions for reading, writing, and processing files, including CSV files for sales reports, receipts, and other relevant data.

📌 Features:
- Read and write sales data to/from CSV files.
- Read and write customer receipt data.
- Handle file management tasks like checking file existence and creating new directories.
- Generate file names with timestamps for easy identification.

🛠️ Dependencies:
- os -> For managing file paths and checking file existence.
- csv -> For reading and writing CSV files.
- datetime -> For generating timestamped filenames.

Functions:
- read_csv_file(file_path: str) -> List[Dict]: Reads a CSV file and returns the data as a list of dictionaries.
- write_csv_file(file_path: str, data: List[Dict]) -> None: Writes data to a CSV file, creating a new file or overwriting the existing one.
- create_directory(directory_path: str) -> None: Creates a new directory if it doesn't exist.
- generate_timestamped_filename(prefix: str) -> str: Generates a timestamped filename for reports or receipts.
- check_file_exists(file_path: str) -> bool: Checks if a file exists at the given path.
"""

import csv
import os
from datetime import datetime
from typing import List, Dict

def read_csv_file(file_path: str) -> List[Dict]:
    """
    Reads a CSV file and returns the data as a list of dictionaries, where each row is a dictionary.
    
    :param file_path: The path to the CSV file.
    :return: A list of dictionaries containing the data from the CSV file.
    """
    data = []
    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    return data

def write_csv_file(file_path: str, data: List[Dict]) -> None:
    """
    Writes data to a CSV file, creating a new file or overwriting the existing one.
    
    :param file_path: The path to the CSV file.
    :param data: A list of dictionaries to write to the CSV file.
    """
    if data:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

def create_directory(directory_path: str) -> None:
    """
    Creates a new directory if it doesn't already exist.
    
    :param directory_path: The path of the directory to create.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def generate_timestamped_filename(prefix: str) -> str:
    """
    Generates a timestamped filename using the given prefix (e.g., for receipts or reports).
    
    :param prefix: The prefix to use for the filename (e.g., 'sales_report').
    :return: A timestamped filename with the format 'prefix_YYYY-MM-DD_HH-MM-SS.csv'.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f"{prefix}_{timestamp}.csv"

def check_file_exists(file_path: str) -> bool:
    """
    Checks if a file exists at the given path.
    
    :param file_path: The path to the file.
    :return: True if the file exists, False otherwise.
    """
    return os.path.exists(file_path)

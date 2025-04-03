"""
string_utils.py

This module provides utility functions for manipulating and processing strings within the Restaurant Management System (RMS).
It includes functions for common string operations such as trimming, formatting, case conversion, and validation.

📌 Features:
- Trim unwanted whitespace from strings.
- Convert strings to different cases (e.g., uppercase, lowercase, title case).
- Check if a string is a valid email address.
- Replace specific characters or substrings within a string.
- Validate string lengths to ensure proper data formatting.

🛠️ Dependencies:
- re -> For regular expressions to validate email addresses and pattern matching.
- string -> For predefined string constants like punctuation and digits.

Functions:
- trim_string(text: str) -> str: Removes leading and trailing whitespace from a given string.
- convert_to_uppercase(text: str) -> str: Converts a string to uppercase.
- convert_to_lowercase(text: str) -> str: Converts a string to lowercase.
- convert_to_title_case(text: str) -> str: Converts a string to title case (capitalizes the first letter of each word).
- is_valid_email(email: str) -> bool: Checks if a given string is a valid email address.
- replace_substring(text: str, old_substring: str, new_substring: str) -> str: Replaces occurrences of a substring with a new substring in a string.
- is_valid_length(text: str, min_length: int, max_length: int) -> bool: Checks if a string's length is within a specified range.
"""

import re
import string

def trim_string(text: str) -> str:
    """
    Removes leading and trailing whitespace from a given string.
    
    :param text: The string to trim.
    :return: A string with no leading or trailing whitespace.
    """
    return text.strip()

def convert_to_uppercase(text: str) -> str:
    """
    Converts a string to uppercase.
    
    :param text: The string to convert to uppercase.
    :return: The string in uppercase.
    """
    return text.upper()

def convert_to_lowercase(text: str) -> str:
    """
    Converts a string to lowercase.
    
    :param text: The string to convert to lowercase.
    :return: The string in lowercase.
    """
    return text.lower()

def convert_to_title_case(text: str) -> str:
    """
    Converts a string to title case (capitalizes the first letter of each word).
    
    :param text: The string to convert to title case.
    :return: The string in title case.
    """
    
    return text.title()


def replace_substring(text: str, old_substring: str, new_substring: str) -> str:
    """
    Replaces occurrences of a substring with a new substring in a string.
    
    :param text: The string where the replacement should occur.
    :param old_substring: The substring to replace.
    :param new_substring: The substring to replace with.
    :return: The modified string with the replacement.
    """
    return text.replace(old_substring, new_substring)

def is_valid_length(text: str, min_length: int, max_length: int) -> bool:
    """
    Checks if a string's length is within a specified range.
    
    :param text: The string to check.
    :param min_length: The minimum length the string should have.
    :param max_length: The maximum length the string should have.
    :return: True if the string length is within the range, False otherwise.
    """
    return min_length <= len(text) <= max_length

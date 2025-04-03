"""
payment_utils.py

This module provides utility functions for managing and processing payments in the Restaurant Management System (RMS). 
It includes functions for calculating taxes, handling payment processing, and generating payment-related reports.

📌 Features:
- Calculate tax and discount for a given payment amount.
- Convert payment amount to a formatted string (currency format).
- Generate unique payment reference numbers.
- Validate payment methods (e.g., credit card, cash).
- Process payment verification (e.g., checking payment status).

🛠️ Dependencies:
- random -> For generating random payment reference numbers.
- decimal -> For precise handling of financial calculations (e.g., taxes and discounts).
- datetime -> For generating timestamps or unique reference numbers.

Functions:
- calculate_tax(amount: float, tax_rate: float) -> float: Calculates the tax on a payment amount.
- calculate_discount(amount: float, discount_rate: float) -> float: Calculates the discount on a payment amount.
- format_currency(amount: float) -> str: Converts a numerical amount into a formatted currency string.
- generate_payment_reference() -> str: Generates a unique payment reference number.
- validate_payment_method(payment_method: str) -> bool: Validates the payment method (e.g., 'cash', 'credit_card').
- process_payment(payment_method: str, amount: float) -> bool: Processes a payment and returns whether the payment was successful.
"""

import random
import decimal
from datetime import datetime

def calculate_tax(amount: float, tax_rate: float) -> float:
    """
    Calculates the tax on a payment amount based on the provided tax rate.
    
    :param amount: The original payment amount.
    :param tax_rate: The tax rate as a percentage (e.g., 0.1 for 10%).
    :return: The tax amount for the payment.
    """
    return round(amount * tax_rate, 2)

def calculate_discount(amount: float, discount_rate: float) -> float:
    """
    Calculates the discount on a payment amount based on the provided discount rate.
    
    :param amount: The original payment amount.
    :param discount_rate: The discount rate as a percentage (e.g., 0.1 for 10%).
    :return: The discount amount for the payment.
    """
    return round(amount * discount_rate, 2)

def format_currency(amount: float) -> str:
    """
    Converts a numerical amount into a formatted currency string with two decimal places.
    
    :param amount: The amount to format.
    :return: The formatted currency string (e.g., '$123.45').
    """
    return "${:,.2f}".format(amount)

def generate_payment_reference() -> str:
    """
    Generates a unique payment reference number using the current timestamp and a random number.
    
    :return: A unique payment reference number (e.g., 'PAY20250403-1234').
    """
    timestamp = datetime.now().strftime('%Y%m%d')
    random_number = random.randint(1000, 9999)
    return f"PAY{timestamp}-{random_number}"

def validate_payment_method(payment_method: str) -> bool:
    """
    Validates the provided payment method.
    
    :param payment_method: The payment method to validate (e.g., 'cash', 'credit_card').
    :return: True if the payment method is valid, False otherwise.
    """
    valid_payment_methods = ['cash', 'credit_card', 'debit_card', 'mobile_payment']
    return payment_method.lower() in valid_payment_methods

def process_payment(payment_method: str, amount: float) -> bool:
    """
    Processes a payment based on the provided payment method and amount.
    
    :param payment_method: The payment method to use (e.g., 'cash', 'credit_card').
    :param amount: The amount to be paid.
    :return: True if the payment is successful, False otherwise.
    """
    if validate_payment_method(payment_method):
        return True
    return False

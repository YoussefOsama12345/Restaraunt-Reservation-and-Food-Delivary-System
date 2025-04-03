"""
Validation Module

This package contains various modules that validate inputs for different parts of the system, including user management, orders, menu, reservations, staff, inventory, billing, and reports.

Modules:
--------
- user_validation: Validates user-related data such as usernames, emails, and roles.
- order_validation: Validates customer order details, including menu items and payment methods.
- menu_validation: Validates menu-related data such as prices, categories, and availability.
- reservation_validation: Validates reservation details such as date, time, and guest count.
- report_validation: Validates report filters and date ranges.
- staff_validation: Validates staff-related data such as employee IDs, shift timings, and salaries.
- inventory_validation: Validates inventory-related data such as stock levels and expiration dates.
- billing_validation: Validates billing-related data such as invoice totals, payment status, and discount codes.

"""

# Import validation modules
from .user_validation import validate_username, validate_email, validate_role, validate_password
from .order_validation import validate_menu_item, validate_payment_method, validate_discount_code
from .menu_validation import validate_price, validate_category, validate_availability
from .reservation_validation import validate_reservation_date, validate_reservation_time, validate_guest_count, validate_table_availability
from .report_validation import validate_date_range
from .staff_validation import validate_employee_id, validate_shift_timing, validate_employee_role, validate_salary
from .inventory_validation import validate_stock_quantity, validate_expiration_date, validate_supplier_details
from .billing_validation import validate_invoice_total, validate_payment_status, validate_discount_code


__all__ = [
    'validate_username', 'validate_email', 'validate_role', 'validate_password',
    'validate_menu_item', 'validate_payment_method', 'validate_discount_code',
    'validate_price', 'validate_category', 'validate_availability',
    'validate_reservation_date', 'validate_reservation_time', 'validate_guest_count', 
    'validate_table_availability','validate_date_range',
    'validate_employee_id', 'validate_shift_timing', 'validate_employee_role', 'validate_salary',
    'validate_stock_quantity', 'validate_expiration_date', 'validate_supplier_details',
    'validate_invoice_total', 'validate_payment_status', 'validate_discount_code'
]

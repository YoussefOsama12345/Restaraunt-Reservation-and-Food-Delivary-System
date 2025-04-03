import win32print
import win32api
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generate_receipt_pdf(receipt_data: dict, output_path: str) -> None:
    """
    Generates a detailed receipt PDF with the provided receipt data, including an order code.
    
    :param receipt_data: A dictionary containing receipt details such as the order code, 
                            customer information, items purchased, total amount, and payment method.
    :param output_path: The path where the generated receipt PDF will be saved.
    """
    c = canvas.Canvas(output_path, pagesize=letter)
    
    add_order_code_to_receipt(c, receipt_data['order_code'])
    add_customer_details_to_receipt(c, receipt_data['customer'])
    add_item_details_to_receipt(c, receipt_data['items'])
    add_payment_details_to_receipt(c, receipt_data['payment_method'], receipt_data['total_amount'])
    add_footer_to_receipt(c, "Thank you for dining with us! Visit again soon.")
    save_pdf(c, output_path)
    print_receipt(output_path)

def print_receipt(pdf_path: str) -> None:
    """
    Sends the generated receipt PDF to the default printer for printing.
    
    :param pdf_path: The path to the PDF file to be printed.
    """
    printer_name = win32print.GetDefaultPrinter()  # Get the default printer
    win32api.ShellExecute(0, "print", pdf_path, '/d:"%s"' % printer_name, ".", 0)

def add_order_code_to_receipt(pdf_canvas: canvas.Canvas, order_code: str) -> None:
    """
    Adds the order code to the receipt at the top.
    
    :param pdf_canvas: The canvas object to add the order code to.
    :param order_code: The unique identifier for the order (e.g., 'ORD12345').
    """
    pdf_canvas.setFont("Helvetica-Bold", 16)
    pdf_canvas.drawString(100, 750, f"Order Code: {order_code}")

def add_customer_details_to_receipt(pdf_canvas: canvas.Canvas, customer_details: dict) -> None:
    """
    Adds the customer's details to the receipt.
    
    :param pdf_canvas: The canvas object to add the customer details to.
    :param customer_details: A dictionary containing customer information like name, address, phone number, etc.
    """
    pdf_canvas.setFont("Helvetica", 10)
    pdf_canvas.drawString(100, 730, f"Customer: {customer_details['name']}")
    pdf_canvas.drawString(100, 710, f"Address: {customer_details['address']}")
    pdf_canvas.drawString(100, 690, f"Phone: {customer_details['phone']}")

def add_item_details_to_receipt(pdf_canvas: canvas.Canvas, items: list) -> None:
    """
    Adds the details of purchased items to the receipt.
    
    :param pdf_canvas: The canvas object to add item details to.
    :param items: A list of dictionaries containing item details (e.g., description, quantity, price).
    """
    y_position = 650  # Start adding items here
    pdf_canvas.setFont("Helvetica", 10)
    
    for item in items:
        pdf_canvas.drawString(100, y_position, item['description'])
        pdf_canvas.drawString(400, y_position, str(item['price']))
        y_position -= 20

def add_payment_details_to_receipt(pdf_canvas: canvas.Canvas, payment_method: str, total_amount: float) -> None:
    """
    Adds the payment details to the receipt.
    
    :param pdf_canvas: The canvas object to add payment details to.
    :param payment_method: The payment method used (e.g., 'Cash', 'Credit Card').
    :param total_amount: The total amount paid for the order.
    """
    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(100, 100, f"Total: {total_amount}")
    pdf_canvas.drawString(100, 80, f"Payment Method: {payment_method}")

def add_footer_to_receipt(pdf_canvas: canvas.Canvas, footer_text: str) -> None:
    """
    Adds a footer with custom text to the receipt.
    
    :param pdf_canvas: The canvas object to add the footer text to.
    :param footer_text: The footer text to display (e.g., a thank you message).
    """
    pdf_canvas.setFont("Helvetica", 8)
    pdf_canvas.drawString(100, 30, footer_text)

def save_pdf(pdf_canvas: canvas.Canvas, output_path: str) -> None:
    """
    Saves the generated PDF receipt to the specified output path.
    
    :param pdf_canvas: The canvas object representing the receipt content.
    :param output_path: The path where the generated receipt PDF will be saved.
    """
    pdf_canvas.save()

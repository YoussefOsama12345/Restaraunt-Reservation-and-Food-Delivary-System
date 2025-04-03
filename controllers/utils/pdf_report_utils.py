"""
pdf_report_utils.py

This module provides utility functions for generating visually appealing PDF reports for the Restaurant Management System (RMS). 
The reports include invoices, sales summaries, and receipts, all of which can be customized with logos, headers, footers, 
tables, and other design elements.

📌 Features:
- Create beautiful and well-structured PDF invoices, sales reports, and receipts.
- Add custom branding with logos, headers, and footers.
- Generate tables with detailed and styled data.
- Easily add custom fonts and colors to enhance the design.

🛠️ Dependencies:
- reportlab -> For creating and manipulating PDF files with rich styling options.
- reportlab.platypus -> For creating tables, paragraphs, and other complex page elements.

Functions:
- generate_invoice_pdf(invoice_data: dict, output_path: str) -> None: Generates a polished invoice PDF based on the provided data.
- generate_sales_summary_pdf(sales_data: list, output_path: str) -> None: Generates a beautifully styled sales summary PDF report.
- add_logo_and_header(pdf_canvas: Canvas, logo_path: str, header_text: str) -> None: Adds a logo and header to the PDF.
- add_table_to_pdf(pdf_canvas: Canvas, table_data: list, column_widths: list) -> None: Adds a formatted table to the PDF.
- add_footer_to_pdf(pdf_canvas: Canvas, footer_text: str) -> None: Adds a footer with custom text to the PDF.
- save_pdf(pdf_canvas: Canvas, output_path: str) -> None: Saves the generated PDF to the specified file path.
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

def generate_invoice_pdf(invoice_data: dict, output_path: str) -> None:
    """
    Generates a PDF invoice based on the provided invoice data with a polished and beautiful design.
    
    :param invoice_data: The dictionary containing invoice details such as items, customer information, and total amount.
    :param output_path: The path where the generated PDF will be saved.
    """
    c = canvas.Canvas(output_path, pagesize=letter)
    
    # Header
    add_logo_and_header(c, invoice_data['logo'], invoice_data['header'])
    
    # Invoice Items and Details
    y_position = 580  # Start adding text here for the invoice items
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.black)
    
    # Add invoice details (items, customer info, etc.)
    for item in invoice_data['items']:
        c.drawString(100, y_position, item['description'])
        c.drawString(400, y_position, str(item['price']))
        y_position -= 20
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y_position, f"Total: {invoice_data['total']}")
    
    # Footer
    add_footer_to_pdf(c, "Thank you for your visit! Contact us at +123-456-7890.")
    
    # Save the PDF
    save_pdf(c, output_path)

def generate_sales_summary_pdf(sales_data: list, output_path: str) -> None:
    """
    Generates a beautiful PDF report summarizing the sales data for a specific period.
    
    :param sales_data: A list of dictionaries containing sales information such as transaction date, amount, and items sold.
    :param output_path: The path where the generated PDF will be saved.
    """
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    
    # Sales Report Title
    story = []
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title = Paragraph("Sales Summary Report", title_style)
    story.append(title)
    
    # Sales Data Table
    table_data = [["Date", "Amount", "Items Sold"]]
    for sale in sales_data:
        table_data.append([sale['date'], sale['amount'], sale['items_sold']])
    
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    
    sales_table = Table(table_data)
    sales_table.setStyle(table_style)
    
    story.append(sales_table)
    
    doc.build(story)

def add_logo_and_header(pdf_canvas: canvas.Canvas, logo_path: str, header_text: str) -> None:
    """
    Adds a logo and a header to the PDF canvas with beautiful alignment and spacing.
    
    :param pdf_canvas: The canvas object to add elements to.
    :param logo_path: The path to the logo image.
    :param header_text: The header text to display at the top of the page.
    """
    pdf_canvas.drawImage(logo_path, 100, 750, width=60, height=60)  # Logo size and position
    pdf_canvas.setFont("Helvetica-Bold", 18)
    pdf_canvas.drawString(200, 780, header_text)

def add_table_to_pdf(pdf_canvas: canvas.Canvas, table_data: list, column_widths: list) -> None:
    """
    Adds a beautifully styled table with data to the PDF report.
    
    :param pdf_canvas: The canvas object to add the table to.
    :param table_data: A list of lists containing the table data.
    :param column_widths: A list specifying the width of each column.
    """
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    
    y_position = 500  # Start table from here
    x_position = 100  # Start table from here
    
    # Add header row first
    for i, column in enumerate(table_data[0]):
        pdf_canvas.setFont("Helvetica-Bold", 10)
        pdf_canvas.drawString(x_position, y_position, str(column))
        x_position += column_widths[i]
    
    y_position -= 20  # Move to the next row
    
    # Add table rows
    for row in table_data[1:]:
        x_position = 100  # Reset to start position
        for i, cell in enumerate(row):
            pdf_canvas.setFont("Helvetica", 10)
            pdf_canvas.drawString(x_position, y_position, str(cell))
            x_position += column_widths[i]
        y_position -= 20  # Move to the next row

def add_footer_to_pdf(pdf_canvas: canvas.Canvas, footer_text: str) -> None:
    """
    Adds a footer with custom text to the PDF with a small font size and neat alignment.
    
    :param pdf_canvas: The canvas object to add the footer to.
    :param footer_text: The footer text to display at the bottom of the page.
    """
    pdf_canvas.setFont("Helvetica", 8)
    pdf_canvas.drawString(100, 50, footer_text)

def save_pdf(pdf_canvas: canvas.Canvas, output_path: str) -> None:
    """
    Saves the generated PDF to the specified file path.
    
    :param pdf_canvas: The canvas object representing the PDF content.
    :param output_path: The path where the generated PDF will be saved.
    """
    pdf_canvas.save()

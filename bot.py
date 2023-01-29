import csv
from email import encoders
from email.mime.base import MIMEBase
import openpyxl
from openpyxl import Workbook
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def main():
    # Step 1: Read data from CSV file
    with open('invoices.csv', 'r') as file:
        data = csv.reader(file)
        invoices = list(data)

    # Step 2: Process invoices data
    for invoice in invoices:
        invoice_number = invoice[0]
        invoice_amount = invoice[1]
        invoice_due_date = invoice[2]

        # Step 3: Create an Excel file for each invoice
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = invoice_number
        sheet['A1'] = "Invoice Number"
        sheet['B1'] = "Invoice Amount"
        sheet['C1'] = "Invoice Due Date"
        sheet['A2'] = invoice_number
        sheet['B2'] = invoice_amount
        sheet['C2'] = invoice_due_date
        workbook.save(f"{invoice_number}.xlsx")

        # Step 4: Send invoice as attachment in an email
        msg = MIMEMultipart()
        msg['From'] = 'your_email@example.com'
        msg['To'] = invoice[3] # email address of the recipient
        msg['Subject'] = f"Invoice {invoice_number}"
        body = f"Please find attached invoice {invoice_number} for the amount of {invoice_amount}. The due date is {invoice_due_date}."
        msg.attach(MIMEText(body, 'plain'))
        filename = f"{invoice_number}.xlsx"
        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('your_email@example.com', 'your_password')
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()

if __name__ == '__main__':
    main()

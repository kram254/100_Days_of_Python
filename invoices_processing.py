import os
import csv

def process_invoices(invoices_directory):
  # Iterate over all files in the invoices directory
  for filename in os.listdir(invoices_directory):
    # Check if the file is a CSV file
    if not filename.endswith('.csv'):
      continue

    # Open the CSV file and read the rows
    with open(os.path.join(invoices_directory, filename)) as csv_file:
      reader = csv.reader(csv_file)
      # Skip the header row
      next(reader)

      # Process each row in the CSV file
      for row in reader:
        invoice_id = row[0]
        customer_id = row[1]
        products = row[2:]

        # Update the inventory levels for the purchased products
        update_inventory(products)

        # Generate a PDF invoice for the purchase
        generate_invoice(invoice_id, customer_id, products)

def update_inventory(products):
  # TODO: Update the inventory levels for the given products
  pass

def generate_invoice(invoice_id, customer_id, products):
  # TODO: Generate a PDF invoice for the purchase
  pass

# Main method
def main():
  invoices_directory = './invoices.csv'
  process_invoices(invoices_directory)

if __name__ == '__main__':
  main()

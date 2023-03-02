import tkinter as tk
from tkinter import ttk
import pyodbc

def onboard_employee(first_name, last_name, email, department):
    # Connect to SQL server
    servername = "your_server_name"
    dbname = "your_database_name"
    cnxn = pyodbc.connect(f"Driver={{SQL Server}};Server={servername};Database={dbname};Trusted_Connection=yes;")

    # Insert new employee into Employees table
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO Employees (FirstName, LastName, Email, Department) VALUES (?, ?, ?, ?)", first_name, last_name, email, department)
    cnxn.commit()

    # Close the database connection
    cnxn.close()

def submit_onboarding_form():
    # Get form data
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    department = department_combobox.get()

    # Onboard new employee
    onboard_employee(first_name, last_name, email, department)

    # Clear the form
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    department_combobox.set("")

# Create main window
root = tk.Tk()
root.title("Employee Onboarding")

# Create form fields
first_name_label = ttk.Label(root, text="First Name")
first_name_entry = ttk.Entry(root)

last_name_label = ttk.Label(root, text="Last Name")
last_name_entry = ttk.Entry(root)

email_label = ttk.Label(root, text="Email")
email_entry = ttk.Entry(root)

department_label = ttk.Label(root, text="Department")
department_combobox = ttk.Combobox(root, values=["Sales", "Marketing", "Engineering", "Operations"])

# Create submit button
submit_button = ttk.Button(root, text="Submit", command=submit_onboarding_form)

# Add form fields and submit button to window
first_name_label.grid(row=0, column=0, padx=5, pady=5)
first_name_entry.grid(row=0, column=1, padx=5, pady=5)

last_name_label.grid(row=1, column=0, padx=5, pady=5)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry.grid(row=2, column=1, padx=5, pady=5)

department_label.grid(row=3, column=0, padx=5, pady=5)
department_combobox.grid(row=3, column=1, padx=5, pady=5)

submit_button.grid(row=4, column=1, padx=5, pady=5)

# Start the main event loop
root.mainloop()
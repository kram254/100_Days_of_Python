import tkinter as tk
from tkinter import ttk, messagebox
import sqlalchemy
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BenefitsEnrollment(Base):
    __tablename__ = 'benefits_enrollment'

    id = Column(String(255), primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    address = Column(String(255))
    phone_number = Column(String(255))
    benefit_plan = Column(String(255))


class BenefitsEnrollmentForm:
    def __init__(self):
        # Connect to the MySQL database
        engine = create_engine(
            'mysql+pymysql://<username>:<password>@<hostname>:<port>/<database>')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

        # Create the tkinter UI
        self.root = tk.Tk()
        self.root.title("Benefits Enrollment Form")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Create the form fields
        ttk.Label(self.root, text="First Name:").grid(
            column=0, row=0, padx=10, pady=10)
        self.first_name = ttk.Entry(self.root)
        self.first_name.grid(column=1, row=0)

        ttk.Label(self.root, text="Last Name:").grid(
            column=0, row=1, padx=10, pady=10)
        self.last_name = ttk.Entry(self.root)
        self.last_name.grid(column=1, row=1)

        ttk.Label(self.root, text="Email:").grid(
            column=0, row=2, padx=10, pady=10)
        self.email = ttk.Entry(self.root)
        self.email.grid(column=1, row=2)

        ttk.Label(self.root, text="Address:").grid(
            column=0, row=3, padx=10, pady=10)
        self.address = ttk.Entry(self.root)
        self.address.grid(column=1, row=3)

        ttk.Label(self.root, text="Phone Number:").grid(
            column=0, row=4, padx=10, pady=10)
        self.phone_number = ttk.Entry(self.root)
        self.phone_number.grid(column=1, row=4)

        ttk.Label(self.root, text="Benefit Plan:").grid(
            column=0, row=5, padx=10, pady=10)
        self.benefit_plan = ttk.Combobox(
            self.root, values=["Plan A", "Plan B", "Plan C"])
        self.benefit_plan.grid(column=1, row=5)

        # Create the submit button
        self.submit_button = ttk.Button(
            self.root, text="Submit", command=self.submit_form)
        self.submit_button.grid(column=0, row=6, columnspan=2, pady=20)

        # Run the tkinter mainloop
        self.root.mainloop()

    def submit_form(self):
        # Get the form data
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        email = self.email.get()
        address = self.address.get()
        phone_number = self.phone_number.get()
        benefit_plan = self.benefit_plan.get()

        # Check if the data has already been submitted
        existing_enrollment = self.session.query(BenefitsEnrollment).filter_by(
            first_name=first_name, last_name=last_name, email=email).first()
        if existing_enrollment:
            tk.messagebox.showerror(
            title="Error", message="This benefits enrollment form has already been submitted.")
        return

        # Create a new BenefitsEnrollment object and add it to the database
        enrollment = BenefitsEnrollment(first_name=first_name, last_name=last_name, email=email,
                                    address=address, phone_number=phone_number, benefit_plan=benefit_plan)
        self.session.add(enrollment)
        
        # Commit the transaction
        self.session.commit()

        # Show a message box to indicate success
        tk.messagebox.showinfo(
        title="Success", message="Your benefits enrollment form has been submitted!")

        # Clear the form fields
        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.phone_number.delete(0, tk.END)
        self.benefit_plan.current(0)  # Reset the combobox to the first value

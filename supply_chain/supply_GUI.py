import tkinter as tk
from tkinter import messagebox
import sqlite3

class SupplyChainManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_tables()

    def _create_tables(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS inventory
                         (sku TEXT PRIMARY KEY, name TEXT, quantity INTEGER)''')
            c.execute('''CREATE TABLE IF NOT EXISTS orders
                         (order_id INTEGER PRIMARY KEY AUTOINCREMENT, sku TEXT, quantity INTEGER, 
                         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
            c.execute('''CREATE TABLE IF NOT EXISTS shipments
                         (shipment_id INTEGER PRIMARY KEY AUTOINCREMENT, sku TEXT, quantity INTEGER, 
                         origin TEXT, destination TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    def add_inventory_item(self, sku, name, quantity):
        try:
            with sqlite3.connect(self.db_path) as conn:
                c = conn.cursor()
                c.execute('INSERT INTO inventory VALUES (?, ?, ?)', (sku, name, quantity))
        except sqlite3.IntegrityError:
            raise ValueError("SKU already exists in inventory")

    def process_order(self, sku, quantity):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('SELECT quantity FROM inventory WHERE sku = ?', (sku,))
            result = c.fetchone()
            if result is None:
                raise ValueError("SKU not found in inventory")
            if result[0] < quantity:
                raise ValueError("Insufficient inventory")
            c.execute('UPDATE inventory SET quantity = quantity - ? WHERE sku = ?', (quantity, SKU))
            c.execute('INSERT INTO orders (sku, quantity) VALUES (?, ?)', (sku, quantity))

    def track_shipment(self, sku, quantity, origin, destination):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute('SELECT quantity FROM inventory WHERE sku = ?', (sku,))
            result = c.fetchone()
            if result is None:
                raise ValueError("SKU not found in inventory")
            if result[0] < quantity:
                raise ValueError("Insufficient inventory")
            c.execute('UPDATE inventory SET quantity = quantity - ? WHERE sku = ?', (quantity, sku))
            c.execute('INSERT INTO shipments (sku, quantity, origin, destination) VALUES (?, ?, ?, ?)', 
                      (sku, quantity, origin, destination))

    def analyze_performance(self):
        # TODO: implement
        pass

class UserInterface:
    def __init__(self, scm):
        self.scm = scm
        self.main_window = tk.Tk()
        self.main_window.title('Supply Chain Management System')
        self.create_gui()

    def create_gui(self):
        self.main_window.geometry('400x400')
        
        # Set the button width and height
        button_width = 15
        button_height = 3
        
        self.add_inventory_button = tk.Button(self.main_window, text='Add inventory item', command=self.add_inventory_item)
        self.add_inventory_button.pack(pady=10)
        
              
        self.track_shipment_button = tk.Button(self.main_window, text='Track shipment', command=self.track_shipment)
        self.track_shipment_button.pack(pady=10)
        
        self.analyze_performance_button = tk.Button(self.main_window, text='Analyze performance', command=self.analyze_performance)
        self.analyze_performance_button.pack(pady=10)
        
        self.process_order_button = tk.Button(self.main_window, text='Process order', command=self.process_order)
        self.process_order_button.pack(pady=10)
        
        self.exit_button = tk.Button(self.main_window, text='Exit', command=self.exit)
        self.exit_button.pack(pady=10)

    def run(self):
        self.main_window.mainloop()

    def add_inventory_item(self):
        try:
            sku, name, quantity = self.get_inventory_data()
            self.scm.add_inventory_item(sku, name, quantity)
            messagebox.showinfo("Success", "Inventory item added successfully")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def process_order(self):
        try:
            sku, quantity = self.get_order_data()
            self.scm.process_order(sku, quantity)
            messagebox.showinfo("Success", "Order processed successfully")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def track_shipment(self):
        try:
            sku, quantity, origin, destination = self.get_shipment_data()
            self.scm.track_shipment(sku, quantity, origin, destination)
            messagebox.showinfo("Success", "Shipment tracked successfully")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            
    def analyze_performance(self):
        self.scm.analyze_performance()

    def exit(self):
        self.main_window.destroy()
        print("Exiting program...")

    def get_inventory_data(self):
        sku = input("Enter SKU: ")
        name = input("Enter name: ")
        quantity = int(input("Enter quantity: "))
        return sku, name, quantity

    def get_order_data(self):
        sku = input("Enter SKU: ")
        quantity = int(input("Enter quantity: "))
        return sku, quantity

    def get_shipment_data(self):
        sku = input("Enter SKU: ")
        quantity = int(input("Enter quantity: "))
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        return sku, quantity, origin, destination

if __name__ == "__main__":
    db_path = "supply_chain.db"
    scm = SupplyChainManager(db_path)
    ui = UserInterface(scm)
    ui.run()
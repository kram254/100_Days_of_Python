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
            c.execute('UPDATE inventory SET quantity = quantity - ? WHERE sku = ?', (quantity, sku))
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

    def run(self):
        while True:
            self.print_menu()
            choice = self.get_choice()

            if choice == 1:
                try:
                    sku, name, quantity = self.get_inventory_data()
                    self.scm.add_inventory_item(sku, name, quantity)
                    print("Inventory item added successfully")
                except ValueError as e:
                    print("Error: " + str(e))

            elif choice == 2:
                try:
                    sku, quantity = self.get_order_data()
                    self.scm.process_order(sku, quantity)
                    print("Order processed successfully")
                except ValueError as e:
                    print("Error: " + str(e))

            elif choice == 3:
                try:
                    sku, quantity, origin, destination = self.get_shipment_data()
                    self.scm.track_shipment(sku, quantity, origin, destination)
                    print("Shipment tracked successfully")
                except ValueError as e:
                    print("Error: " + str(e))
                         
            elif choice == 4:
                self.scm.analyze_performance()

            elif choice == 5:
                print("Exiting program...")
                break

    def print_menu(self):
        print("\nSupply Chain Management System")
        print("1. Add inventory item")
        print("2. Process order")
        print("3. Track shipment")
        print("4. Analyze performance")
        print("5. Exit")

    def get_choice(self):
        while True:
            try:
                choice = int(input("\nEnter choice: "))
                if choice < 1 or choice > 5:
                    print("Invalid choice. Please enter a number between 1 and 5.")
                else:
                    return choice
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

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

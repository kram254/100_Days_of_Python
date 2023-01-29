from rpa import *

def data_entry():
    # Connecting to the database
    conn = database.connect(
        driver='sqlite',
        database='mydb.sqlite'
    )

    # Creating a new table in the database
    conn.execute('''CREATE TABLE customers
                 (name TEXT, email TEXT, address TEXT)''')

    # Reading data from a spreadsheet
    data = read_spreadsheet('customers.xlsx')

    # Inserting data into the database
    for row in data:
        conn.execute("INSERT INTO customers (name, email, address) VALUES (?,?,?)",
                     (row['name'], row['email'], row['address']))

    # Closing the connection
    conn.close()

if __name__ == "__main__":
    data_entry()

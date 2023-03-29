import sqlite3
import pandas as pd
from rpa import *

def main():
    # Load the input CSV file into a Pandas DataFrame
    input_df = pd.read_csv('input.csv')

    # Create a connection to the SQLite database
    conn = sqlite3.connect('example.db')

    # Loop through each row of data in the input DataFrame
    for index, row in input_df.iterrows():
        try:
            # Extract the data from the row using Pandas
            name = row['Name']
            address = row['Address']
            phone = row['Phone']
            email = row['Email']

            # Validate the accuracy of the data using Pandas
            if pd.isna(name) or pd.isna(address) or pd.isna(phone) or pd.isna(email):
                raise ValueError('Missing data')

            if len(name) < 2:
                raise ValueError('Name is too short')

            if len(address) < 5:
                raise ValueError('Address is too short')

            if not pd.api.types.is_string_dtype(phone):
                raise ValueError('Phone is not a string')

            if len(phone) < 10:
                raise ValueError('Phone number is too short')

            if not pd.api.types.is_string_dtype(email):
                raise ValueError('Email is not a string')

            if '@' not in email:
                raise ValueError('Invalid email address')

            # Insert the data into the SQLite database using Pandas
            data = {'name': [name], 'address': [address], 'phone': [phone], 'email': [email]}
            df = pd.DataFrame(data)
            df.to_sql('contacts', conn, if_exists='append', index=False)

        except ValueError as e:
            # Handle validation errors gracefully
            send_notification("Error: " + str(e))

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()

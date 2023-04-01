# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Carrie Liu
# carrihl1@uci.edu
# 64814057

def main_menu():
    print("Welcome to the DSU Management System")
    print("1. Create a new DSU file")
    print("2. Load an existing DSU file")
    print("3. Admin mode")
    print("4. Exit")
    user_input = input("Please select an option: ")
    if user_input == "1":
        create_dsu()
    elif user_input == "2":
        load_dsu()
    elif user_input == "3":
        admin_mode()
    elif user_input == "4":
        exit()
    else:
        print("Invalid input. Please try again.")
        main_menu()
        
def create_dsu():
    file_name = input("Enter the file name: ")
    if file_exists(file_name):
        print("File already exists. Loading the file.")
        load_dsu(file_name)
    else:
        # Code to create a new DSU file
        print("File created successfully.")
        main_menu()
        
def load_dsu(file_name=None):
    if file_name is None:
        file_name = input("Enter the file name: ")
    if file_exists(file_name):
        # Code to load an existing DSU file
        print("File loaded successfully.")
        main_menu()
    else:
        print("File not found. Please try again.")
        load_dsu()
        
def file_exists(file_name):
    # Code to check if file exists
    return False
        
def admin_mode():
    print("Entering admin mode. Type 'exit' to return to the main menu.")
    while True:
        admin_input = input("Enter a command: ")
        if admin_input == "exit":
            main_menu()
        else:
            # Code to handle admin commands
            print("Command executed successfully.")

if __name__ == "__main__":
    main_menu()

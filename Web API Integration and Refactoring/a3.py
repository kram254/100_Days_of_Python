# a3.py
# Carrie Liu
# carrihl1@uci.edu
# 64814057

import os
import re
import sys
import ds_client
import ds_protocol
from profile import Profile


class Journal:
    """Class representing a local journal."""

    def __init__(self):
        """Create a new Journal object with an empty list of entries."""
        self.entries = []

    def add_entry(self, entry):
        """Add a new entry to the journal."""
        self.entries.append(entry)

    def print_entries(self):
        """Print all entries in the journal."""
        if not self.entries:
            print("No entries to display.")
        else:
            for i, entry in enumerate(self.entries):
                print(f"Entry {i+1}:")
                print(entry)

    def save_entries(self, filename):
        """Save all entries in the journal to the specified file."""
        with open(filename, 'w') as f:
            for entry in self.entries:
                f.write(entry + "\n")
        print(f"Journal entries saved to {filename}.")


class JournalInterface:
    """Class representing a command line interface for
       interacting with a Journal object."""

    def __init__(self):
        """Create a new JournalInterface object."""
        self.profile = None
        self.journal = None
        self.commands = {
            "create": self.create_profile,
            "login": self.login,
            "logout": self.logout,
            "add": self.add_entry,
            "print": self.print_entries,
            "save": self.save_entries,
            "server": self.change_server,
            "bio": self.change_bio,
            "post": self.post_entry
        }

    def run(self):
        """Start the command line interface."""
        print("Welcome to your journal!")
        while True:
            if self.profile:
                username = self.profile.username
                prefix = f"{username} >> "
            else:
                prefix = ">> "
            command = input(prefix)
            if not command:
                continue
            tokens = command.split()
            if tokens[0] not in self.commands:
                print("Invalid command.")
            else:
                self.commands[tokens[0]](tokens[1:])

    def create_profile(self, args):
        """Create a new user profile."""
        if self.profile:
            print("You are already logged in."
                  "Please logout to create a new profile.")
        else:
            print("Please provide a username and password.")
            username = input("Username: ")
            password = input("Password: ")
            while Profile.username_exists(username):
                print("That username is already taken."
                      "Please choose another one.")
                username = input("Username: ")
            self.profile = Profile(username, password)
            print(f"Profile for {username} created.")

    # def create_profile(self, username, password):
    #     """Create a new profile with the specified username and password."""
    #     # Check if a profile with the same username already exists
    #     if os.path.exists(username + ".pkl"):
    #         print("A profile with that username already exists.")
    #         return
    #     # Create the new profile
    #     self.profile = Profile(username, password)
    #     self.profile.save()
    #     print(f"Profile created for user {username}.")

    def login(self, args):
        """Log in to an existing user profile."""
        if self.profile:
            print("You are already logged in.")
        elif len(args) < 2:
            print("Please provide a username and password.")
        else:
            username = args[0]
            password = args[1]
            if not Profile.username_exists(username):
                print("That username does not exist.")
            else:
                profile = Profile.load_profile(username)
                if profile.password_matches(password):
                    self.profile = profile
                    self.journal = Journal()
                    self.journal.entries = ds_client.get_entries(
                        username, password)
                    print(f"Logged in as {username}.")
                else:
                    print("Incorrect password.")

    def logout(self, args):
        """Log out of the current user profile."""
        if not self.profile:
            print("You are not logged in.")
        else:
            self.profile = None
            self.journal = None
            print("Logged out.")

    def add_entry(self, args):
        """Add a new entry to the journal."""
        if not self.profile:
            print("You must be logged in to add an entry.")
        else:
            if not self.journal:
                self.journal = Journal()
            entry = input("Enter your journal entry: ")
            self.journal.add_entry(entry)
            print("Entry added to journal.")

    def print_entries(self, args):
        """Print all entries in the journal."""
        if not self.profile:
            print("You must be logged in to view entries.")
        elif not self.journal:
            print("No entries to display.")
        else:
            self.journal.print_entries()

    def save_entries(self, args):
        """Save all entries in the journal to a file."""
        if not self.profile:
            print("You must be logged in to save entries.")
        elif not self.journal:
            print("No entries to save.")
        elif not args:
            print("Please provide a filename to save to.")
        else:
            filename = args[0]
            self.journal.save_entries(filename)

    def change_server(self, args):
        """Change the server that journal entries are posted to."""
        if not self.profile:
            print("You must be logged in to change servers.")
        elif len(args) < 2:
            print("Please provide a server hostname and port number.")
        else:
            hostname = args[0]
            try:
                port = int(args[1])
            except ValueError:
                print("Invalid port number.")
            else:
                self.profile.change_server(hostname, port)
                print("Server changed.")

    def change_bio(self, args):
        """Change the user's biography."""
        if not self.profile:
            print("You must be logged in to change your bio.")
        elif len(args) < 1:
            print("Please provide a new bio.")
        else:
            bio = ' '.join(args)
            self.profile.change_bio(bio)
            print("Bio changed.")

    def post_entry(self, args):
        """Post a journal entry to the server."""
        if not self.profile:
            print("You must be logged in to post entries.")
        elif not self.journal:
            print("No entries to post.")
        else:
            if not ds_client.server_available(self.profile.server_hostname,
                                              self.profile.server_port):
                print("Server is not available.")
            else:
                for entry in self.journal.entries:
                    success, message = ds_protocol.post_entry(
                        self.profile, entry)
                    if success:
                        print("Entry posted.")
                    else:
                        print(f"Posting failed: {message}")
                self.journal = None


if __name__ == "__main__":
    JournalInterface().run()

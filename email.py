import imaplib
import email

# Connect to the email server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Log in to the email account
username = input("Enter your email address: ")
password = input("Enter your email password: ")
mail.login(username, password)

# Select the inbox
mail.select("inbox")

# Search for unread emails
status, messages = mail.search(None, 'UNSEEN')
messages = messages[0].split()

# Loop through the emails
for message in messages:
    # Get the email data
    status, data = mail.fetch(message, "(RFC822)")
    msg = email.message_from_bytes(data[0][1])

    # Print the subject and sender of the email
    print("Subject:", msg["Subject"])
    print("From:", msg["From"])

    # Mark the email as read
    mail.store(message, "+FLAGS", "\\Seen")

# Close the connection
mail.close()
mail.logout()

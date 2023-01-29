from uipath import EmailMessage

def main():
    #Reading the email
    email = EmailMessage.Read("Inbox")

    #Extracting the subject and body of the email
    subject = email.Subject
    body = email.Body

    # Defining list of keywords for different categories
    keywords = {
        "billing": ["invoice", "payment", "bill"],
        "shipping": ["delivery", "tracking", "shipment"],
        "returns": ["refund", "return", "exchange"]
    }

    # Initializing variable to store the category
    category = " "

    # Iterating through the keywords
    for key, values in keywords.items():
        for value in values:
            if value in subject or value in body:
                category = key
                break
        if category != " ":
            break

    # Defining dictionary of departments
    departments = {
        "billing": "billing@companymail.com",
        "shipping": "shipping@companymail.com",
        "returns": "returns@companymail.com"
    }

    # Getting appropriate departmen email 
    to_email = departments[category]

    # Forwarding email to the appropriate department
    email.Forward(to_email)

    # Defining a dictionary of FAQs and responses
    faqs = {
        "How can I track my order?": "You can track your order by visiting our website and entering your tracking number.",
        "What is your return policy?": "Our return policy can be found on our website. If you have any further questions, please contact our returns department."
    }

    # Iterating through the FAQs
    for question, answer in faqs.items():
        if question in body:
            email.Reply(answer)
            break

if __name__ == "__main__":
    main()

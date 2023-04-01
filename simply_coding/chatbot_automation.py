import aa_sdk
import smtplib

def main():
  # Connecting to RPA's Automation Anywhere
  aa = aa_sdk.AutomationAnywhere()

  # Sending a message to the chatbot
  response = aa.send_message_to_chatbot("How was the business productivity for today?")

  # Sending  email to the manager with the response
  server = smtplib.SMTP('smtp.example.com')
  
  server.login("mark_ndaliro@gmail.com", "Pass1234")
  
  server.sendmail("mark_ndaliro@gmail.com", "my_manager@gmail.com", response)
  
  server.quit()

if __name__ == '__main__':
  main()

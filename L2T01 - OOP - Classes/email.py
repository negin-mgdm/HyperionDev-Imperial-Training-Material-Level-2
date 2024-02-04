### --- OOP Email Simulator --- ###
# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email :
    
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
       self.email_address = email_address
       self.subject_line = subject_line
       self.email_content = email_content    
       
    # Create the method to change 'has_been_read' emails from False to True.       
    def mark_as_read(self):
        self.has_been_read = True
        
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for the program.
def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    email_1 = Email("abc@gmail.com", "Utility Bill", "Hi, Please see attached this month's utility bill.")
    email_2 = Email("friend@yahoo.com", "Birthday", "Happy birthday my dear!")
    email_3 = Email("xyz@gmail.com", "Successful registration", "Dear customer, You have successfully registered.")
    inbox.extend([email_1, email_2, email_3])

# Create a function which prints the email’s subject_line, along with a corresponding number.
def list_emails():
    for count, value in enumerate(inbox):
        print(count, value.subject_line)
      

# Create a function which displays a selected email. 
# Once displayed, call the class method to set its 'has_been_read' variable to True.
def read_email(index):
    email = inbox[index]
    email.has_been_read = True
    print(f"\nYou have one email from {email.email_address} Subject: '{email.subject_line}' \n {email.email_content} \n marked as read.\n")
 
# --- Email Program --- #
# Call the function to populate the Inbox for further use in the program.
populate_inbox()

# Initialize the menu loop and start a while loop to repeatedly display the menu to the user.
menu = True
while menu:
    # Display the menu options and get the user's choice
    user_choice = int(input('\n' + "Would you like to:" +'\n' 
                             + "1. Read an email" + '\n' + "2. View unread emails"
                             + '\n' + "3. Quit application" + '\n' + "Enter selection: "))
    
    # If the user chooses to read an email; list available emails for selection.
    if user_choice == 1:
        list_emails()
        email_num = int(input("Which email would you like to read, number 0, 1 or 2? "))
        read_email(email_num)
    
    # If the user chooses to view unread emails; filter the inbox to get unread emails.    
    elif user_choice == 2:
        unread_emails = list(filter(lambda email : email.has_been_read == False, inbox))
 
        if len(unread_emails) == 0:
            print("There are no unread emails. ")
        else:
            print("Unread emails are as follows: ")
            for email in unread_emails:
                if email.has_been_read == False:
                    print(f"Email subject: {email.subject_line}")
               
    # If the user chooses to quit the application; exit the loop.
    elif user_choice == 3:
        exit()
        
    # Handle invalid input
    else:
         print("Oops - incorrect input.")


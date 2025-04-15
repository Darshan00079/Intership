import re
test_emails =input("Enter the email to validate: ")

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        print(f"{test_emails} is a valid e-mail address")
        return 0
    else:
        print(f"{test_emails} is an invalid e-mail address")
        return 0

is_valid_email(test_emails)
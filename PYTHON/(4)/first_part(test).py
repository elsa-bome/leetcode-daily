from find_name_start import find_first_email
from find_name_end import find_last_email

def find_emails(text):
    
    first_part = find_first_email(text)
    if first_part == '':
        return None
    print(first_part)

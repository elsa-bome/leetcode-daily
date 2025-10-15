
from find_name_start import find_first_email
from find_name_end import find_last_email

def find_emails(text):

    try:
        last_part = find_last_email(text)
        print(last_part)
    except TypeError: 
        return None
    last_part = print(None)
   

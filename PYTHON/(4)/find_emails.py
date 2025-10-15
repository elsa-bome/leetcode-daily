#basuppgift 1

from find_name_start import find_first_email
from find_name_end import find_last_email

def find_emails(text):

    first_part = find_first_email(text)
    if first_part == '':
        return None
    
    last_part = find_last_email(text)
    if last_part == '':
        return None
    
    #if first_part == None:
     #   return text[None: last_part]
    #if last_part == None:
     #   return text[first_part: None]
    #else:
    print(first_part + last_part)
    
        
    

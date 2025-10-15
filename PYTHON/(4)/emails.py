#basuppgift 1

#import re
from find_name_start import find_first_email 
from find_name_end import find_last_email 

def find_emails(text):
    first_part = find_name_start(text)
    last_part = find_name_end(text)
    print('first_part' + 'last_part')

#emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
#print (emails)

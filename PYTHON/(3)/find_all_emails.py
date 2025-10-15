#basuppgift 2

from email_from_string import email_from_string
from both import find_first_email

def split_text(text):
    if type(text)!=str or len(text)==0:
        print("Invalid input, enter text with spaces")
        return ""
    word_list = text.split()
    return word_list

text = 'svara till joachim@hotmail.com eller pelle@gmail.com' #@hi #joachim@hotmail.com
def find_all_emails(text):
    new_text = split_text(text)
    length_new_text = len(new_text)
    #print('a', length_new_text)
    i = 0
    emails = []

    while i < length_new_text:
        email = email_from_string(new_text[i])
        #print('e',email)
        if email == (None, None):
            pass
        else:
            emails += [email[0]]
        i += 1
    return emails
    

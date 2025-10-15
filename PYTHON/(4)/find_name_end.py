import string
EMAIL_CHARS = string.ascii_letters + string.digits + '.'

def find_name_end(text, at_index):
    first_index = 0
    for index in range(at_index-1, -1, -1): #baklänges!
        if text[index] not in EMAIL_CHARS:
         first_index = index + 1
         break
    return first_index

def find_last_email(text):
    at_index = text.find('@')
    if at_index < 0:
        return None

    name_end = find_name_end(text, at_index) 
    if name_end == at_index:
        return None

    return text[at_index+1:]

import string
EMAIL_CHARS = string.ascii_letters + string.digits + '.'

text='svara till joachim@hotmail.com eller pelle@gmail.com'

#hitta index där första namnet börjar
def find_name_start(text, at_index):
    first_index = 0
    for index in range(at_index-1, -1, -1): #baklänges!
        if text[index] not in EMAIL_CHARS:
         first_index = index + 1
         break
    return first_index

#hitta index där första namnet slutar
def find_name_end(text, at_index):
    text = text + ' '
    last_index = 0
    for index in range(at_index,len(text), 1): #baklänges!
        if text[index+1] not in EMAIL_CHARS:
         last_index = index + 1
         break
    return last_index

#hitta första epostadress
def find_first_email(text):
    at_index = text.find('@')
    if at_index < 0:
        return None

    name_start = find_name_start(text, at_index)
    name_end = find_name_end(text, at_index) 
    if name_end == at_index:
        return None
    if name_start == at_index:
        return None
    result= text[name_start : at_index+1]+ text[at_index+1:name_end ]
    return result

def test_find_first_email(text):
    test_lists = ['svara till joachim@hotmail.com eller pelle@gmail.com hej hellu', 'eller pelle@gmail.com','svara till joachim@ho','@gmail', '.se', '@@gmail.com', 'idaåäö@gmail.com','',' ','t','6','?@454=/&#%¤"', 'ida@@gmail.com']
    for test in test_lists:
        print('test',test)
        result = find_first_email(test)
        print(test ,'has email', result)
        print()

    at_index = text.find('@')
    if at_index < 0:
        return None



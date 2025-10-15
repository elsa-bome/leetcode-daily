#basuppgift 1
from both import find_name_start,find_name_end,find_first_email

text='svara till joachim@hotmail.com eller pelle@gmail.com' #@hi joachim@hotmail.com #hej@ #@hej 

def email_from_string(text):
    email = find_first_email(text)

    if email == None:
        check_at_exist = text.find('@',0,len(text))
        if check_at_exist == -1:
            return email, None
        else:
            r = text.replace('@','',1)
            return email, r

    else:
        if email in text:
            checkindex = text.index(email)
            #print('a',checkindex) 
            start = 0
            stop = checkindex-1
            newtext = text[0: start:] + text[stop + 1::]
            #print('b',newtext) 
            checkexist = newtext.find(' ',checkindex,len(newtext))
            #print('c',checkexist) 
            newtextt = text[checkindex::] 
            #print('d',newtextt)
            newtextt = newtext[checkexist + 1::] 
            #print('e',newtextt)
            if checkexist < 0:
                newtextt = None
            #print('d',newtextt)
            return email, newtextt
    

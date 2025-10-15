#övn 5
def strip_of_characters(text):
    if type(text)!=str:
        print("Input must be text")
        return
    counter=0
    text_list=list(text)
    text_remove=[]
    for character in text_list:
        if character.isalpha()==True: break
        counter+=1
    del text_list[:counter]
    if len(text_list)==0:
        return 
    text_list=list(reversed(text_list))
    counter=0
    for character in text_list:
        if character.isalpha()==True: break
        counter+=1
    del text_list[:counter]
    text_list=list(reversed(text_list))
    join_char=""
    text_list=join_char.join(text_list)
    return text_list

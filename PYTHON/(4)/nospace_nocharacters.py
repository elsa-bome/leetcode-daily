#övn 6
from strip_of_characters import strip_of_characters
from split_text import split_text
def nospace_nocharacters(text):
    if type(text)!=str:
        pass
    text_split=split_text(text)
    #print("text_split", text_split)
    words_nocharacters=[]
    for split_element in text_split:
        words_nocharacters.append(strip_of_characters(split_element))
    return words_nocharacters

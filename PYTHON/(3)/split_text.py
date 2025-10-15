#övn 4
# Ett ord definieras som något sammansatt av alfabetiska bokstäver och
# inget mellanslag
def split_text(text):
    if type(text)!=str or len(text)==0:
        print("Invalid input, enter text with spaces")
        return ""
    word_list= text.split()
    return word_list
    
    

#övn 9,10
def printout_letters(word):
    if type(word)!=str:
        print("Value must be a string")
        return
    dictionary={}
    for letter in word:
        if letter in dictionary:
            pass
        else:
            dictionary[letter]= 0
    list_of_keys=dictionary.keys()
    list_of_keys=list(list_of_keys)
    list_of_keys.sort()
    the_letters="".join(list_of_keys)
    return the_letters

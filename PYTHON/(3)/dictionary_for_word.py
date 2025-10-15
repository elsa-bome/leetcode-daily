#övn 8
def dictionary_for_word(word):
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
    the_letters="".join(list_of_keys)
    print(the_letters)
    return dictionary

from random import *
def first_word(dictionary):
    first_word=[]
    dictionary_keys=list(dictionary.keys())
    random_number=randint(0,len(dictionary_keys)-1)
    random_key=dictionary_keys[random_number]
    first_word=random_key
    return first_word

from random import *
def following_word(key,dictionary):
    values=dictionary[key]
    if len(values)==0:
        print("HhuiohguIOHUIOGUI")
    keys=dictionary.keys()
    length_keys=len(keys)
    random_number=randint(0,len(values)-1)
    next_word=values[random_number]
    return next_word


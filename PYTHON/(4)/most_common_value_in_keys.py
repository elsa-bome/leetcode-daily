from count_words import count_words
from word_max_presence import word_max_presence
def most_common_value_in_keys(maxword,dictionary):
    list_dictionaries_words_after_word=[]
    for word in maxword:
        list_dictionaries_words_after_word.append(count_words(dictionary[word]))
    max_word_after_word=[]
    for dictionary in list_dictionaries_words_after_word:
        max_word_after_word.append(word_max_presence(dictionary))
    return max_word_after_word
    #print(max_word_after_word)
        #Gå igenom alla ord
        #for word_after_word in dictionary[word]:
            #if len(dictionary[key].values())==max_key[0]:
             #print(word_after_word)   
    return

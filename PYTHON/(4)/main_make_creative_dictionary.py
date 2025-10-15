from files_smalltext_nocharacters import files_smalltext_nocharacters
from word_max_presence import word_max_presence
from count_words import count_words
from most_common_value_in_keys import most_common_value_in_keys
def main_make_creative_dictionary(file):

    #Make dictionary:
    word_list=files_smalltext_nocharacters(file)

    #Make creative wordlist:
    dictionary={}
    counter=0
    for word in word_list:
        if counter==len(word_list)-1: break
        if word in dictionary:
            dictionary[word]+=[word_list[counter+1]]
        else:
            dictionary[word]=[word_list[counter+1]]
        counter+=1
    
    #Find most common word/words:
    word_dictionary_count=count_words(word_list)
    maxword=word_max_presence(word_dictionary_count)
    print("Most common words: ", maxword, "\n(Word/words which text contains most of)")


    #Which words follows the 'most common words' mostly?
    most_common_word_after_maxword= most_common_value_in_keys(maxword[0],dictionary)
    print("\nWords which follow most often:", most_common_word_after_maxword)
    print("(These words are the most common word which follows directly after the 'most common words' above")
    return

from files_smalltext_nocharacters import files_smalltext_nocharacters
from count_words import count_words
from word_max_presence import word_max_presence
def countwords_and_maxword(file):
    word_list=files_smalltext_nocharacters(file)
    print("Toal word count: ", len(word_list),"\n")
    word_dictionary_count=count_words(word_list)
    print("Category word count: ",len(word_dictionary_count), "\n(same word not counted more than one time)\n")
    maxword=word_max_presence(word_dictionary_count)
    print("Word count max: ", maxword, "\n(Word/words which text contains most of)")
    return

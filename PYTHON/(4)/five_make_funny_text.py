from files_smalltext_nocharacters import files_smalltext_nocharacters
def five_make_funny_text(file):

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
    

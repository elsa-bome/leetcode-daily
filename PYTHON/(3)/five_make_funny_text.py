from openfiles import openfiles
from split_text import split_text
from random import *
from first_word import first_word
from following_word import following_word
def five_make_funny_text(file,length):

    #Make dictionary:
    file_content=openfiles(file)
    if len(file_content)==0:
        print("Files contains nothing, or contains no spaces")
        return
    word_list=split_text(file_content)
    #print("length", len(word_list))
    if len(word_list)==1:
        print("Files contains nothing, or contains no spaces")
        return
    #print(type(word_list))

    #Make dictionary wordlist:
    dictionary={}
    counter=0
    for word in word_list:
        if counter==len(word_list)-1: break
        if word in dictionary:
            dictionary[word]+=[word_list[counter+1]]
        else:
            dictionary[word]=[word_list[counter+1]]
        counter+=1

    #Bestämmer första ordet 
    word_one=first_word(dictionary)
    funny_text=[]
    funny_text.append(word_one)
    #print(dictionary)
    

    #Loop som går lägger till så många ord som angivet
    present_word=word_one
    dictionary_keys=dictionary.keys()
    #print(dictionary_keys)
    #print(word_list)
    for i in range(1,length):
        next_word=following_word(present_word,dictionary)
        #Checks if it's the last word(has no following words)
        if next_word==word_list[len(word_list)-1]:
            #print("Problem")
            next_word=first_word(dictionary)
            i=1
        present_word=next_word
        #Makes new word have big first letter
        if i==1:
            next_word=list(next_word)
            next_word[0]=next_word[0].upper()
            next_word="".join(next_word)
        funny_text.append(next_word)
    #print("what")

    
    #Makes first letter big, adds dot, make list into string
    funny_text[0]=list(funny_text[0])
    funny_text[0][0]=funny_text[0][0].upper()
    funny_text[0]="".join(funny_text[0])
    funny_text=" ".join(funny_text)
    funny_text=[funny_text]
    funny_text.append(".")
    funny_text="".join(funny_text)
    #print("Result:", funny_text)
    return funny_text

#övn 12
#from count_words import count_words
def word_max_presence(dictionary):
    if type(dictionary)!=dict:
        print("Value must be a dictionary")
        return
    #print(dictionary)
    max_number=list([0])
    max_word=list([])
    #print(type(max_number))
    for word in dictionary:
        #print(dictionary[word])
        #print(type(max_number))
        if dictionary[word] == max_number[0]:
             max_number.append(dictionary[word])
             max_word.append(str(word))
        if dictionary[word] > max_number[0]:
            max_number=list([dictionary[word]])
            max_word=list([word])
    if max_number==[0]:
        print("Value must be a string")
        return
    return max_word, max_number

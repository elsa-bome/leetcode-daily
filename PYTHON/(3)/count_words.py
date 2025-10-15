#övn 11
def count_words(thelist):
    if type(thelist)!=list:
        print("Value must be a list")
        return
    dictionary={}
    for word in thelist:
        if word in dictionary:
            dictionary[word]+=1
        if word not in dictionary:
            dictionary[word]=1
    #del dictionary[" "]
    #testgrej
    #list_values=dictionary.values()
    #print(list(list_values))
    #type(list_values)
    #testgrej
    return dictionary


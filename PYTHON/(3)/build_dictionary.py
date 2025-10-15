def build_dictionary():
    imported_file = open('file.txt','r')
    with open('file.txt', 'r') as f:
        for line in f:
           list_of_words = line.replace(',','').split()
           key_tup = tuple(list_of_words)
           value_tup = tuple(list_of_words)
           dictionary_1 = dict(zip(key_tup,value_tup))
    dictionary_2 = {}
    
    for key_tup,value_tup in dictionary_1.items():
        if value_tup not in dictionary_2:
            dictionary_2[value_tup] = [key_tup]
        else:
            dictionary_2[value_tup].append(key)
    print(dictionary_2)
    
        

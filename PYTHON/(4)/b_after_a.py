#förberedande övning 5

def b_after_a(text):
    if type(text)!=str:
        print('Value must be a string')
        return
    
    index_position_a = text.find('a')
    if index_position_a == -1:
        print('text does no contain a')
        return
    else:
        print('a index position is:',index_position_a)
        
    index_position_b = text.find('b')
    if index_position_b == -1:
        print('text does no contain b')
        return
    else:
        print('b index position is:',index_position_b)

    if index_position_a < index_position_b:
        return True
    else:
        return False

  
    
   

#förberedande övning 7

def between(text, a, b):
    
    # Find and validate before-part.
    pos_a = text.find(a)
    if pos_a == -1:
        print('text does not contain a')
        return 

    # Find and validate after part.
    pos_b = text.find(b)
    if pos_b == -1:
        print('text does not contain b')
        return 
    
    # Return middle part.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b:
        print('b comes before a, try again!')
        return 
    return text[adjusted_pos_a:pos_b]

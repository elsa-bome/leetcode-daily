from sequence_length import*
def function_value():
    n=1
    max = 0
    while n <= 50:
        length = sequence(n)
        print(n, 'has sequence length', length)
        if length > max:
            max = length
            maxat = n
        n += 1     
    print('maximum at', maxat, 'is', max)

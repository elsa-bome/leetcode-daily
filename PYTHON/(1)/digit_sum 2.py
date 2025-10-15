def digit_sum(pnumber):                                 
    sum = 0                                 
    while pnumber > 0:                      
        lastdigit = pnumber % 10            
        sum = sum + lastdigit
        print('e',sum)
        pnumber = pnumber // 10
        print('f',pnumber)
    return sum                              

from digit_sum import *
n=1
while n < 10000:
    sum = digit_sum(n)
    if sum**3 == n:
        print(n)
    n+=1

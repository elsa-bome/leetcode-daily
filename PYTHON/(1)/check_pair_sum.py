A = [1, 2, 4, 5]
x = 2
i = 1
j = length(A)

while i <= j:
    if S[i] +S[j] == x + 1:
    return True
    if S[i] +S[j] < x + 1:
        i=i+1
    else:
        j=j+1
return False

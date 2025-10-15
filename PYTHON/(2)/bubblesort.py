def bytintill(li):
	byttplats = False
	for index in range(len(li)-1):
		if li[index] > li[index+1]:
		    temp=li[index]
		    li[index] = li[index+1]
		    li[index+1]=temp
		    byttplats = True
	return byttplats

def bubblesort(li):
    while bytintill(li) == True:
        bytintill(li)
    return li


import random
randomlist = random.sample(range(1,100),10)
print('randomlist',randomlist)
sortedlist = bubblesort(randomlist)
print('sortedlist',sortedlist)

from is_sorted import*
def does_it_work():
        if is_sorted(sortedlist) == True:
                print('The list is sorted. It Works')
        else:
                print('The list is not sorted. It does not work')

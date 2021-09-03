'''for num in range(10):
    print(num)
    
#range(start with, upto,number of gap)
for num in range(1,10):
    print(num)
    
for num in range(1,10,5):
    print(num)
    
#creating list
print(list(range(1,11,2)))
#creating tuple
print(tuple(range(1,11,2)))

#counting the index of string
index_count = 0
for letter in "ALOK KUMAR KAUSHAL":
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1
    
#Using Enumerate in place of index and letter you can use item
word = 'Alok kumar kaushal'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')'''
    
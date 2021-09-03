#that is wrong but use as design pyramind
"""mystr='hello'
mylist=[]
for letter in mystr:
    mylist.append(letter)
    print(mylist)"""
    
mystr='hello'
mylist=[]
for letter in mystr:
    mylist.append(letter)
print(mylist)

#or
mylist=[letter for letter in mystr]
print(mylist)

#exaple 2
mylst=[letter for letter in 'word']
print(mylst)

#creating rang
rng=[num for num in range(1,10)]
print(rng)

#creating a square
sqr=[num**2 for num in range(0,10)]
print(sqr)
''' or use this code 
mystr=range(0,10)
mylist=[]
for letter in mystr:
    mylist.append(letter**2)
print(mylist)'''

#get even number from range
rng=[num for num in range(0,10) if num%2==0]
print(rng)

#get square of even number
rng=[num**2 for num in range(0,10) if num%2==0]
print(rng)
mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num) #now num will print from 1 to 10
    
for num in mylist:
    print('hello')  #this hell will print upto 10 times
    
#now let suppose we want to print only even number from this list 
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')
        
#let try to calculate sum of all number in given list
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(f'Sum of all number is: {list_sum}')

#but let i want to add every single like 1, (1+2)=3,(3+3)=6,(6+4)=10
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(f'Sum of all number is: {list_sum}')
    
#let print  a string 
mystring = 'Hello World'
for mystr in mystring:
    print(mystr)
    
#tuple in for loop
tup = (1,2,3,4,(5,6,7))
for item in tup:
    print(item)
    
#let example 2 of tuple
myl = [(1,2),(3,4),(5,6),(7,8),(9,10)]
print(len(myl))
for item in myl:
    print(item)
    
#now if i want to print every single num in new line then
for (a,b) in myl:
    print(a)
    print(b)

#let this nested
mylst=[(1,2,3),(4,(0,5,6),15),(7,8,(9,10,11))]
print(len(mylst))
for a,b,c in mylst:
    print(a)
    print(b)
    print(c)
    
#dict
mylist = {'k1':1,'k2':2,'k3':3}
for item in mylist:
    print(item) #here we only get keys 
    
#for getting key and value
for item in mylist.items():
    print(item)

#let get individual detail of value or key
for key, value in mylist.items():
    print(key)
    print(value)
    
# you can get result of only value
for value in mylist.values():
    print(value) 
    

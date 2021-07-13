#et create new list
list1=[1,2,3]

#append
'''
adding new value/element in list, append always add in end of list
'''
list1.append(4)
#print(list1)

#count
'''
count tell number of time that element are present
'''
print(list1.count(2))

#extend
'''
this append elements from the iterable,not created a list form
'''
x=[1,2,3]
x.extend([4,5])
#print(x)

#index
'''
index() will return the index of any element as placed in argument, but element not found in list cases error, also it is not started with index 0
index 2= value 1
'''
#print(list1.index(3))

#insert
'''
this will take 2 argument,index and obj, to help to place obj at the given obj
'''
list1.insert(2,'inserted')
#print(list1)

#pop
'''
delet element from last place,but passing index help to delet element from given index place
'''
ele=list1.pop(1)
#print(ele)#show deleted element

#remove
'''
remove() help to remove first occurence of value
'''
list1.remove('inserted')
#print(list1)
list2=[1,2,3,4,3,5]
list2.remove(3)
print(list2)

#reverse
list2.reverse()
print(list2)

#sort
'''
sort() sort the list
'''
list2.sort()
print(list2)

#reverse sort()
list2.sort(reverse=True)
print(list2)

'''
*------------- problem in appending and solution    ---------*
'''
x=[1,2,3]
y=x.append(4)
print(y)#here we get none
'''
we first need to make a copy of list x to y and then modify
'''
x=[1,2,3]
y=x.copy()
y.append(4)
print(y)
#let create empty set first then add values init
s=set()
'''
using add() we will add values in empty set
'''
s.add(1)
s.add(2)
#print(s)

#   Clear
#s.clear()
#print(s)    #return set() actually all values get cleared

#   Copy
s={1,2,3}
sc=s.copy()
#print(s)#before adding new value
s.add(4)
s.add(5)
#print(s)#after adding new value
#print(sc)#there is no effect on copy means both work seprately
'''
copy() return a copy of set, what ever we can do on copy never effect origional set
'''

#   Difference
#print(s.difference(sc))
'''
difference() will give the difference between set1 and set 2, like here 4 and 5 are not in sc
'''
a={1,2,3,4}
b={5,6,9}
#print(b.difference(a))

#   Difference Update
s1={1,2,3}
s2={1,4,5}
s1.difference_update(s2)
print(s1)
'''
set1.difference_update(set2), the method return set1 after removingelement found in set
'''

#   Discard
s={1,2,3,4,5}
s.discard(3)
#print(s)
'''
removes an element from a set if it is a member. if not then do nothing
'''

#   intersection and intersection_update
'''
this return the intersection of two or more set as a new set,which is having common element of both set
'''
a1={1,2,3}
a2={1,2,5}
#print(a1.intersection(a2)) #if there is nothing then simply return set()
a1.intersection_update(a2)
#print(a1)

#   Isdisjoint
'''
this return True if two set have null intersection
'''
b1={1,2}
b2={1,2,4}
b3={5}
#print(b1.isdisjoint(b3))
#print(b2.isdisjoint(b1))

#   Subset
'''
this will report wether another set contain this set
'''
c1={1,2,3,4}
c2={1,2,3}
#print(c1.issubset(c2))

#   Issuperset
#print(c1.issuperset(c2))

#   Symmetric_difference
'''
this will give the value which is not in one of set
'''
#print(c2.symmetric_difference(c1))

#   Union
'''
combine all elements in one
'''
#print(c1.union(c2))

#   Update
c1.update(c2)
print(c1)
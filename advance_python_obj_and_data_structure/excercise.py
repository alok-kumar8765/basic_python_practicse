#   Convert 1024 to binary
print(bin(1024))
print(hex(1024))

#   2 palce round of 5.23222
print(round(5.23222,2))

#   check if every letter in str is lowercase
s='hello how are you Mary,are you feeling okay'
print(s.islower())

#   how many time w showup
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

#   find element that is not in set2
set1={2,3,1,5,6,8}
set2={3,1,7,5,6,8}
print(set1.difference(set2))

#   find all element that are in either set
print(set1.union(set2))

#   create a dict of multiple2 0 to 8
a={x:x**3 for x in range(5)}
print(a)

#   reverse list
list1=[1,2,3,4]
list1.reverse()
print(list1)

#   sort list
list2=[3,4,2,5,1]
list2.sort()
print(list2)
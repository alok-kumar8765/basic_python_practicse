result = 100/777
print("the result was {}".format(result))
''' float format me "{value:wiidth.precision f}" use hota hai, valuse yani result kya show krna hai, width mtalb kitna white space dena hai, aur precision mtlb kitna place ka float vlaue show krna hai, last me f float ke liye '''
print("the result was {r:5.3f}".format(r=result))


# f-string method
#Example 1
name= "jose"
print(f" hello, his name is {name}")

#example2
name='raj'
age=18
print(f'{name} is {age} years old')

lst=[0,1,2]
print(lst.pop())

lt=['a','b','c']
print(lt[1:])
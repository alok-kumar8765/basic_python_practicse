'''
It is used for numeric connection to value as well as name connections to value
'''
from collections import namedtuple
Dog=namedtuple('dog',['breed','age','name'])
sam= Dog(age=5,breed='husky',name='sam')
print(sam)

# Example 2
name_tuple=namedtuple('fruit','like,dislike')
values_in_tuple=name_tuple('mango','pineapple')
print(values_in_tuple)
# with this you can show key value pair systmatic
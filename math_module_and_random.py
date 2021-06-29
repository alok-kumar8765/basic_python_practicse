import math
val=4.75
val2=5.35
val3=7.92
print(math.floor(val))
print(math.floor(val2))
print(math.floor(val3))
'''
The floor gives the previos value, what ever written before . that will be output
'''
print(math.ceil(val))
print(math.ceil(val2))
print(math.ceil(val3))
'''
The ceil modules give nex number
'''
val=4.45
val2=6.69
val3=7.69
print(round(val))
print(round(val2))
print(round(val3))

#mathematical constant
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
print('\n End of Mathematical Constant')

#logarithmic values
print(math.log(100,10)) #log(x,base)
print(math.log(10))
print(math.e**2.302585092994046)
print(math.log(math.e))
print('\n End of Logarithmic Values')

#Trignometrics functions
print(math.sin(10))
from math import pi
print(math.degrees(pi/2))
print(math.radians(180))
print('\n End of Trignometrics Functions')

#Seed method
'''
We know hw random works, but if you want to show/output a random number
which shows same in any system, or print same time o f random value every time
then this seed is used
'''
import random
random.seed(101) #note this line of code always used befor random.randit and 101 will any orbitary number
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print('\n End of random.seed()')

#Random Sequence
mylist=list(range(0,20))
print(mylist)
#you can grab random item from list but it's not parmanently effacted
print(random.choice(mylist))
'''
But what if you want to grab more then one item from list.
there are 2 methods for this,
    1-Sampling with replacement: 
    2-Sample without replacement:means if item once picked then it will not picked again
'''
#method 1
print(random.choices(population=mylist,k=10))
'''
population is the denoted that from where you want to picking it and k=10 denoted how many items you need
'''
#Method 2 : Sample without Replacement
print(random.sample(population=mylist,k=10))
print(mylist)
# to shuffle this arranged list
random.shuffle(mylist)
print(mylist)
print('End of Random Sequence \n')

#Uniform
'''
this is used to pick a random float number between we assign
'''
print(random.uniform(a=0,b=100))
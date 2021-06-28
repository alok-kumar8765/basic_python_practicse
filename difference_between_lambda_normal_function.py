'''
Lambda Function: It is an anonymous function or a function having no name, where you will use the lambda keyword, it is one liner code.That make a different from regular normal function.
It is having 3 part.
1-Lambda keyword
2-parameter
3-function body
A lambda function can have any number of parameter but the function body can only caontain one expression.
Syntax: labda arguments: expression
'''
# Example 1
adder = lambda x,y: x+y
print(adder(5,2))

# Letss try to return string
str = ' This is some kind of string'
print(lambda str: print(str))
'''
Here we define a string that you will pass as a parameter to lambda. Lambda itself return a function object
Here lambda function is not being called by the print function but simply returing the function object and stored in memory which location is shown on consol.
'''
#Lets try to pring string
x = 'This is a string '
(lambda x:print(x))(x)
'''
Here we are defining lambda and calling it immediately by passing the string as an argument
'''

# Function
'''
A function is a block of code which only runs when it's callled.
you can pass data, known as parameter into function.
A function can return data as result, and it can defined with def keyword, how it is differ from lambda? actually you can use as many function as you need
nested, or outside and call again.
''' 
# Example of simple function
def my_func():
    print('Hello world')
my_func() 

# Lets  Take a Fileter Function and trying on normal function and lambda
list1 = ['a','b','i','c','e','o','z','u']
print(list(filter(lambda x: x[0] in "aeiou", list1)))

#Same hing with normal function
letter = ['a','b','i','c','e','o','z','u']
def filter_vowel(letter):
    vowels=['a','e','i','o','u']
    if(letter in vowels):
        return True
    else:
        return False
filtered_vowel= filter(filter_vowel,letter)
print('the filtered vowels are: ')
for vowel in filtered_vowel:
    print(vowel)

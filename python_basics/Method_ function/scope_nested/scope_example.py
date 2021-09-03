#suppose you assign value in x outside function
"""x=25

#now you create a function and there is also a x variable
def printer():
    x=50
    return x
print(x)    #just to check whether it give 25 aur 50
print(printer())

#Example 2
name ='This is a Global Variable '
def greet():
    #enclosing function
    name = 'ARYAN'
    
    def hello():
        print('Hello ' + name)
        
    hello()
greet()
print(name)"""

#Example 3 modify global or enclose valiable
y=5
#Global
def function1():
    z=10
    #enclose variable
    print('initial value of z ;',z)
    def inner1():
        x=10
        nonlocal z
        z+=z
        print('x : ',x)
        print('modified value of z',z)
    inner1() 
    print(z)
function1()

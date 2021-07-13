# Hexadecimal
'''
To use this function you can simply write hex(), within paranthesis 
put any number, and get hexa decimal coverted number.
'''
#a=int(input('enter your number to convert into hexa:    '))
#print(f'The hexa decimal value of {a}:' + hex(a) +'\n')

#   Binary
'''
To convert any number into binary simply use bin(),
put any value within paranthesis
'''
#b=int(input('Enter any number to convert into binary:   '))
#print(f'The binary value of {b}:    '+bin(b)+'\n')

#   Exponentials
'''
This function pow() take two arguments, a to the power y and third is mode
(x^y)%z
'''
#c1=int(input('Enter any integer value:  '))
#c2=int(input('Enter the power:  '))
#c=pow(c1,c2)
#print(f'The {c1} of power {c2} is equal:    {c}'+'\n')

#print(pow(5,2,3))
#so now here 5 is the value we need their to multiply,2 is power, and 3 is mode

#   Absolute Value
'''
This will return absolute value of a number.Argument can be int,
float or complex.but in complex number magnitude is required
'''
'''
d=float(input('Enter your desired number: '))
d1=abs(d)
print(f'The absolute value of {d}:   {d1}'+'\n')

d= abs(19 + 21j) #trying to convert complex to abs()
print(d)
print('\n')
x = 19.21e1/2 # exponential to abs()
print(abs(x))
print('\n')
y = 0b1100 # binary to abs()
print(abs(y))
print('\n')
z = 0o11 # octal to abs()
print(abs(y))
print('\n')
w = 0xF # hexadecimal to abs()
print(abs(w))
print('\n')
'''

#   Round
'''
The round( gives the precise decimal value)
'''
print(round(3.955,1))
#here 3.955 is the float value we want to round off, 1 is the place after or how many place we need to round off 
#round(number, number of digits)
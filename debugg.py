'''
As in example 1 you can print your code and check where the error occure and set teace before that line
and simply check variables,result and result2 you will get to know the reason or error.
'''
import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

'''
Here in example 2 you just set trace before your code, now you can use few features like,n for next line,
every time you press n it will gives first variable details then shows r1 and r2 and gives you the error on line.
you can directly jump to error line using c, thats shows error and quit automatically,and there is l that show in which line you are currently and last q for quit
'''
# Set a trace using Python Debugger
pdb.set_trace()

result2 = y+x
print(result2)

#example 2
pdb.set_trace()
x=10
y=2
z=0

r1=x+y
r2=x/y/z
print(r1)
print(r2)

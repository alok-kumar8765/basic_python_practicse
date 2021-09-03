''' In Print Format we use 2 methos, 1- .format()
2-f-string'''
print('this is a string{}'.format('INSERTED'))
print('the {} {} {}' .format('fox','brown','quick'))
print('the {2} {1} {0}' .format('fox','brown','quick')) #if you put index number then out put will come according to them
print('the {0} {0} {0}' .format('fox','brown','quick'))
print('the {q} {b} {f}' .format(f='fox',b='brown',q='quick')) #if you want you can give variable value put in curly brace to understand
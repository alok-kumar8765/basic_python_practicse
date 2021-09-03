def add(a,b):
    c=a+b
    print('add() executed under the scope: ', __name__)
    return c
if __name__ == '__main__':
    x=input('Enter the first number to add: ')
    y=input('Enter the secode number to add: ')
    result = add(int(x),int(y))
    print(x, '+', y,'=', result)
    print('Code executed under the scope: ', __name__)

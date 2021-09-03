def ran_check(num,low,high):
    return num in range(low,high+1)   #include last number in range +1 added
print(ran_check(5,2,7))     #this will give true or false

def check_ran(n,l,h):
    if n in range(l,h+1):
        print(f'{n} is in range of {l} and {h}')
    else:
        print('not in range')
check_ran(9,1,15)
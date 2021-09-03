def div(func):
    def wrap(a,b):
        print('we are dividing',a,'with',b)
        if b == 0:
            print('OOps .. Can not divide')
            return
        else:
            return func(a,b)
    return wrap
@div
def go_div(a,b):
    return a/b

print(go_div(20,2))
print(go_div(20,0))
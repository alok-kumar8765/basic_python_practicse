def func(f):
    def wrapper(*args,**kwargs):
        print('Start')
        rv=f(*args,**kwargs)
        print('Ended')
        return rv
    return wrapper
@func
def func2(x,y):
    print(x)
    return y
func2(6,5)

#example 2
def deco(funct):
    def wrap(**kv):
        for k,v in kv.items():
            s=kv.pop(k)
            kv[k]=s.upper()
        funct(**kv)
    return wrap
@deco
def display(**kwargs):
    print(kwargs)

d={'name':'alok','add':'varanasi'}
display(**d)
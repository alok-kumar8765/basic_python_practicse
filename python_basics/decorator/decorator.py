def new_deco(original_func):
    def wrap_func():
        print('Some Extra code before original Function')
        original_func()
        print('Some extra code after original function')
    return wrap_func
@new_deco
def func_need_deco():
    print('I Want to be decorated')
    
func_need_deco()
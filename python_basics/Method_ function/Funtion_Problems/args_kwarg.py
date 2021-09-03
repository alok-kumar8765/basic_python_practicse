#normal argument
def function_1(name,age,rollno):
    print(type(name))
    print("The name of the student is ",name, "and age is", age,"roll number is",rollno)
function_1("raj",22,3456)
print(type(function_1("raj",22,3456)))

#using args
def function_2(*args):
    print(type(args))
    print("The name of the student is ",args[0], "and age is", args[1],"roll number is",args[2])
#exaple2
def function_3(*args):
    print(type(args))
    if(len(args)==3):
        print("The name of the student is ",args[0], "and age is", args[1],"roll number is",args[2])
    else:
        print("the name of student is ",args[0],"and age is",args[1])
        
lis=["alok",22,3568]
result=function_3(*lis)
print(type(result))

#kwargs
def function_4(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
lst={'leo':100,'lex':97,'abhi':77}
function_4(**lst)

#passing 3 argumen, 1-normal,2-args and then 3-kwargs
def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)
lis=['leo',22,86934]
lst2={'leo':100,'lex':97,'abhi':77}

master('normal arg',*lis,**lst2)
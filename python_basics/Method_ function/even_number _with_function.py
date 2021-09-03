def even_num(num):
    return num % 2 == 0
result=even_num(20)
print(result)

def check_even_list(num_list):
    for number in num_list:
        if number % 2 ==0:
            return True
        else:
            pass
    return False
x=check_even_list([1,2,3])
print(x)

#Return all Positive even number
def retu_even_num(num_list):
    even_num=[]
    for number in num_list:
        if number%2==0:
            even_num.append(number)
        else:
            pass
    return even_num
x=retu_even_num([1,2,3,4,5,6,7,8,9])
print(x)
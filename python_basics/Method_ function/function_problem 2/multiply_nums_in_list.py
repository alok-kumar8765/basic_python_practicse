def multiply(number):
    total=1
    for num in number:
        total=total*num
    return total
print(multiply([1,2,3,-4,10]))
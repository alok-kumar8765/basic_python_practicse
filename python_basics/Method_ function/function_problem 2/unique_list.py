#method 1
def unique_list(lst):
    return list(set(lst))
print(unique_list([1,1,1,2,2,3,5,6,7,7,4,2,10,10,9]))

#method 2
def uin_list(lst):
    seen_number=[]
    for number in lst:
        if number not in seen_number:
            seen_number.append(number)
    return seen_number
print(unique_list([1,1,1,2,2,3,5,6,7,7,4,2,10,10,9]))

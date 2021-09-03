'''def old_macdonal(name):
    if(len(name)>3):
        return name[:3].capitalize()+name[3:].capitalize()
    else:
        return 'Name is too short'
print(old_macdonal('macdonal'))

def old_macdonald(name):
    letters = list(name)
    for index in range(len(name)):
        if index == 0:
            letters[index] = letters[index].upper()
        elif index == 3:
            letters[index] = letters[index].upper()
    return " ".join(letters)
print(old_macdonal('hellothere'))

def old_macdonald(name):
    mylist = list(name)
    mylist[0] = mylist[0].upper()
    mylist[3] = mylist[3].upper()
    return ''.join(mylist)
print(old_macdonal('hellothere'))'''

#easy method
def cap_letter(name):
    first_letter = name[0]
    inbetween =name[1:3]
    fourth_letter=name[3]
    rest=name[4:]
    return first_letter.upper() + inbetween + fourth_letter.upper() + rest
print(cap_letter('hellothere'))
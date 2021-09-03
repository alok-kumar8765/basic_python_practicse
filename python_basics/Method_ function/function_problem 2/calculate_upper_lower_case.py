def up_low(s):
    #method 1
    lowercase=0
    uppercase=0
    
    for char in s:
        if char.isupper():
            uppercase +=1
        elif char.islower():
            lowercase +=1
        else:
            pass
    print(f'original string: {s}')
    print(f'lowercase count : {lowercase}')
    print(f'uppercase count : {uppercase}')
s='Hello There, My Name Is Lucifer'
up_low(s)

#using dictionary
def up_low(s):
    d={'upper':0,'lower':0}
    for char in s:
        if char.isupper():
            d['upper'] +=1
        elif char.islower():
            d['lower'] +=1
        else:
            pass
    print(f'original string: {s}')
    print(f"lowercase count : {d['lower']}")
    print(f"uppercase count : {d['upper']}")
s='Hello There, My Name Is Lucifer'
up_low(s)

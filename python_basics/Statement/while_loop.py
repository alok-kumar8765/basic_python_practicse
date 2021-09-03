'''x = 0
while x < 10:
    print(f'The current value of x is : {x}')
    x = x + 1
    #x += 1
else:
    print('its done')

#pass
x = [1,2,3,4]
for item in x:
    pass
print('end of line')

#continue
mystr='banana'
for letter in mystr:
    if letter=='a':
        continue
    print(letter)

#break
mystr='alok'
for letter in mystr:
    if letter=='o':
        break
    print(letter)'''
x = 0
while x<5:
    if x==2:
        break
    print(x)
    x+=1
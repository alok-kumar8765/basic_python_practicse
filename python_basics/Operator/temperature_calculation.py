celcius=[0,10,20,30,40,50,60,50.5,34.9]
fahrenheit=[((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

#or
fahrenheit=[]
for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))
print(fahrenheit)
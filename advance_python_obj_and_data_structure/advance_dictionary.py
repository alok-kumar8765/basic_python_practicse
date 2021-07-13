#create dict comprihension
a={x:x**2 for x in range(10)}
print(a)

#   Iteration over keys, values and item
d={'k1':1,'k2':2}
for k in d.keys():
    print(k)    #show all keys
for v in d.values():
    print(v)    #show all value
for item in d.items():
    print(item) #show key value pair 

#Viewing keys, values and items
key_view=d.keys()
print(key_view)

#adding new key value
d['k3']=3
print(key_view)
value_view=d.values()
print(value_view)
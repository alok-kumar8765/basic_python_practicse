mylist=[]
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)

mylist=[x*y for x in [2,4,6] for y in [1,10,100]]
print(mylist)
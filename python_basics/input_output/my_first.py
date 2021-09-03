myfile=open('my_first.txt')
print(myfile)
print(myfile.read())
print(myfile.seek(0))   #some time .read give blank when use countinously so seek helps to rest it and next time when .read used there will no error or blank comes
print(myfile.readlines())
clo=myfile.close()
print(clo)
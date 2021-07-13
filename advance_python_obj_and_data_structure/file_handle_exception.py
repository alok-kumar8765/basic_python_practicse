'''
p=open('oops.txt','a')
p.readlines()
p.close()

#let modify file
p.write('add more text')
p.close()

'''
#protect file with try/except/finally
p=open('oops.txt','a')
try:
    p.readlines()
except:
    print('an exception raised')
finally:
    p.close()
p.write('add more text')

# save step with with
with open('oops.txt','a') as p:
    p.readlines()
p.write('add more text')
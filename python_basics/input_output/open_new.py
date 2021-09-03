myfile=open('my_first.txt')
'''with open('my_first.txt') as my_new_file:
    contents=my_new_file.read()
    print(contents)'''

'''with open('my_first.txt', mode='a') as f:
    f.write('This Is Appended Line')
with open('my_first.txt', mode='r') as f:
    print(f.read()) '''
    
with open('alok.txt', mode='w') as f:
    f.write('I have created this new file')
with open('alok.txt', mode='r') as f:
    print(f.read())
    
    
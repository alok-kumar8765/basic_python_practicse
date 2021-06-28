'''
As we have already learn about how to find current directory by using command pwd but in python there is a buit-in function that we can import, which is import os,
It allows us to do open/read/write and even move or files which will make to ease to handling our files.
'''
#Know your Current Directory
import os
os.getcwd()

#To know list of directories 
os.listdir() #this will give you list of all current directory

#You can pass in any directory
os.listdir("C:\\Users")

#Move file using shutil
'''
but there is a restriction or condition, if you login your system as user xyz, and when you trying to move file, there will be a permission restrictions
syntax:
import shutil
shutil.move('your file name','location you want to move')
'''
import shutil
shutil.move('test.txt','C:\\Users')
print('This is my first repository')

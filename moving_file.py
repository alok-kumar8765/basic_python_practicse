'''
This will help to move file from dir to any dir
'''
import shutil
shutil.move('test.txt','C:\\Users\\alokk\\OneDrive\\Documents\\python_basics')

'''
If you want t delete file/folder there are 3 way, but these are dangerous once's you delete then it will not recover
so better first install send2trash, this help to recover your file, because after delete files stored in trash 
which you later restore.
'''

#First returned back our moved file
import os
import shutil
import send2trash
#print(os.listdir()) #we can see test.txt is nit avialable
#print(shutil.move('C:\\Users\\alokk\\OneDrive\\Documents\\python_basics\\test.txt',os.getcwd()))
#to get back file, 'first location of file where it is save' then after comma get.cwd()
send2trash.send2trash('test.txt') #now the file send to trash means partially deleted
print(os.listdir())


file_path='E:\\Work_Station\\Complete-Python-3-Bootcamp-master\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\Example_Top_Level'
for folder,sub_folders,files in os.walk(file_path): #tuple unpacking
    print(f'currently working directory{folder}')
    print('\n')
    print('The sub folders are :')
    for subfolder in sub_folders:
        print(f'subfolder are: {subfolder}')
    print('\n')
    print('The files are :')
    for f in files:
        print(f'the files : {f}')
    print('\n')
    '''
    This will help to showing the top to down level folder, sub folder and files under them
    '''
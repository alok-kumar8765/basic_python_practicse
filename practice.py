#***** unzip file *************
import shutil
from typing import Pattern
shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')
#let try to open with python
with open('extracted_content/Instructions.txt') as f:
    content =f.read()
    print(content)
'''
unzip_me_for_instructions.zip= it represent the name of zip file present in current directory,which detect automatically
''= means to extract contant in default current dir and extracted content is default folder name
'''

#************ In txt file there is telephone number, we have to search match with help of os module and regular expression**************
import re
pattern = r'\d{3}-\d{3}-\d{4}'
test_string='here is a phone number 123-222-1234' #just to check wether it is working on not in this string
re.findall(pattern,test_string)

def search(file,patpattern = r'\d{3}-\d{3}-\d{4}'):
    f=open(file,'r')
    text=f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ""
#now we have to search in all file in foler to do so use os module
import os
result=[]
for folder,sub_folders,files in os.walk(os.getcwd()+'\\extracted_content'):
    for f in files:
        full_path= folder+'\\'+f
        result.append(search(full_path))
for r in result:
    if r !='':
        print(r.group())
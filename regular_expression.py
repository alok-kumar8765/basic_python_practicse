'''
we know that we can search for substring withing a large string with in operator.

'''
import re
from typing import Text

text='The agent phone number is 000-000-0000. call soon'
'phone' in text # as we know it will give true

pattern='phone'
match=re.search(pattern,text)
print(match)
'''
There is a one problem with search, if you have mutiple matches in string it will only return the first one
'''

txt='i have a phone, my phone number is xxx-xxx-xxx, you can call on my phone'
match=re.search('phone',txt)
print(match)

'''
To get all match we use find all, this wil give list of all matches as many times they come in txt
'''
match=re.findall('phone',txt)
print(match)

'''
Now if you want to know at what index this matches found you have to iterate this
'''
match=re.finditer('phone',txt)
for matches in match:
    print(matches)
    
#or you can write in below way
for match in re.finditer('phone',txt):
    print(match)
print('End of basics of regular expression \n')

#***********  Identifier  **********
txt2 = ' My phone number is 0542-555-12345'
phone = re.search('0542-555-12345',txt2) #Now here we know the number so simply search for match
print(phone)
#but now lets try to find number as we dont know 
phone2=re.search(r"\d\d\d\d-\d\d\d-\d\d\d\d\d",txt2)
print(phone2)
print(phone2.group) # this will give the phone number

#use quantifier
phone3=re.search(r"\d{3}-\d{3}-\d{5}",txt2)
print(phone3)
print('End od quntifier \n')

#******* Cmpile use ***********
'''
Bascally if you want to see individual part of phone number like aear code you have to first compile this
which help to make singular now indexing in group help to get desired postion vale
one thing keep in mind here index start with 1
'''
patt=re.compile(r"(\d{3})-(\d{3})-(\d{5})")
result=re.search(patt,txt2)
print(result)
print(result.group())
print(result.group(1))

#**************** Additinal RegEx Syntax*********
print(re.search(r'cat|dog','the dog is here.cat')) #This help to search either a is in string or b, if both found, first value will show
print(re.findall(r".at",'the cat sat at the walt,cat at shat'))
print(re.findall(r'^\d','1 hello'))

#******************* Exclude ************
txt='there are 3 number in 34 present 5 in this line'
patt=r'[^\d]+'
print(re.findall(patt,txt))

txt2='this is a string! it has punctuation.what i do?'
patt=r'[^!.?]+'
print(re.findall(patt,txt2))

#************ Inclusion*******************
txt=" This is a hyponeted-word, here we use hypo-word in sentence, hypo-sen"
patt=r'[\w]+-[\w]+'
print(re.findall(patt,txt))

t1='hello, there is catfish'
t2='would you like catnap'
t3='have you see this caterpiller'
print(re.search(r"cat(fish|nap|erpiller)",t3))
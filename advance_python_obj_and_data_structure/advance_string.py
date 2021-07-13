#let take a str and try to do many things
abc='hello techqware, how are you'
#   Capitalize
'''
This function help to cap the first  word of str
'''
#print(abc.capitalize())

#Upper
'''
This function is used to caps the all letter of word in str
'''
#print(abc.upper())

#lower
#print(abc.lower())

#Location and Countng
'''
count help to give report how many time any str/word,letter occur
'''
#print(abc.count('o'))

'''
the find function return the starting position of first occurence
'''
#print(abc.find('o'))

#   Center Formatting
'''
using center() we can put our str inbetween we provided str with a certain length
'''
#print(abc.center(50,'a'))
#here 'a' is str which going to place at starting and end, and note only single letter will used
#50 is total length, means len of abc str and len of, if here we give 10 then only abc str will show

#   Expandtabs
'''
This method is used to expand tab \t
'''
#print('hello\tTechqware,\tHow are you'.expandtabs())
abc='hello world'
#   Is Check Method
#print(abc.isalnum())
'''
isalnum return True if all char in abc are alphanumeric,if 2 or more words having space then return False
'''
#print(abc.isalpha())
'''
isalpha return True if all char in abc are alphabetic,if 2 or more words having space then return False
'''
#print(abc.islower())
'''
islower return True if all cased char in abc are lowercase,If any word having single upper case then return False
'''
#print(abc.isspace())
'''
isspace return Ture if all char having whitespace
'''
#print(abc.istitle())
'''
istitle return True only when abc is title case and there is atleast one char in abc, or uppercased cahr and lowercase char only cased ones, rst all time return False 
'''
#print(abc.isupper())
'''
isupper method return True if all cased char in abc are upper case
'''
#print(abc.endswith('d'))
'''
endwith return true when str end with that assign letter matched
'''

#   Regular Expression
#print(abc.split('e'))
'''
abc.split actually split from our assign letter e,that letter e will not included
'''
print(abc.partition('l'))
'''
partition used to create partition from the letter we assign and that will also included
'''

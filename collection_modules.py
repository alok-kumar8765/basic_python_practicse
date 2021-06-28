from collections import Counter
mylist = [1,1,1,1,1,2,2,2,2,2,2,3,3,4,4,4,4,4,4,5,5,5,5,6] #Count how mnay 1s or 2s are ther
'''
There is one way use for loop and have some sort of dict then check is number already seen or not.If seen then go add count+1
if haven't seen creat a new key and add 1 etc.
But Counter is easy way
'''
print(Counter(mylist)) #Notice it will return dict way output
#Example 2
print(Counter('aaaaaaaabbcccc')) # Youc can check hownay times a occurs which will shown in dic

# Example 3
sentence = ' How many times does these words shows up in this sentence '
x=Counter(sentence.split())
print(x)

'''
Lets understand .most_common()
'''
letters = 'aaaaabbbbbbbccccddddeeeeeeeeeee'
c=Counter(letters)
print(c.most_common()) # This will show normal result as it up till shown
print(c.most_common(2)) # this one give you 2 most higher time comes alphabates
print(list(c)) #This will gives the key means those alphabates name in letter
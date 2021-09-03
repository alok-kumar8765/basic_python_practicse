import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    print(alphaset)
    str1 = str1.replace(' ','')
    print(str1)
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaset
print(ispangram("The quick brown for jumes over bed"))
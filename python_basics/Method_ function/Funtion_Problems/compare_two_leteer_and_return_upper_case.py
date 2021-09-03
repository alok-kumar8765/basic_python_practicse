def animal_cracker(text):
    wordlist = text.split()
    return wordlist[0][0]== wordlist[1][0]
print(animal_cracker('level lamba'))            #this show only first letters are either upper or lower
def cracker(text):
    wordlist=text.lower().split()
    print(wordlist)
    return wordlist[0][0]== wordlist[1][0]
print(cracker('Crazy cat'))
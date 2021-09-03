# Q- GIVEN SENTENCE, RETURN A WORDS REVERSED
def master_yoda(text):
    return ' '.join(text.split()[::-1])
print(master_yoda('i am home'))

def rever_sent(sentence):
    words=sentence.split(' ')
    rever_sent=' '.join(reversed(words))
    return rever_sent
print(rever_sent('i am home'))
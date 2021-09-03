class Dog:
    def __init__(self,breed):
        self.breed=breed
#sam=Dog(breed='lab')
#frank=Dog(breed='husky')
#print(sam.breed)

#example 2
class Dog:
    species='mammal'
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
sam=Dog('lab','sam')
print(sam.name)
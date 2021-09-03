class Dog:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+'say woof'
class Cat:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+'says meow'
niko=Dog('niko')
flex=Cat('flex')
print(niko.speak())
print(flex.speak())
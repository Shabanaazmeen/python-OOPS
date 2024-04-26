#polymorphism
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "wolf!"
class Cat(Animal):
    def speak(self):
        return "meow"
class Cow(Animal):
    def speak(self):
        return "mow!"
def make_Animal_speak(Animal): 
    print(Animal.speak())  

dog =Dog()
cat=Cat()
cow=Cow()
make_Animal_speak(dog)     
make_Animal_speak(cat)   
make_Animal_speak(cow)   
    


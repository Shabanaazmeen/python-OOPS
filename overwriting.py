class Animal:
    def speak(self):
        return "Animal makes a sound"
    
class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Cow(Animal):
    pass
    
dog=Dog()
cat=Cat()
cow=Cow()

print("Dog says:",dog.speak())
print("cat says:",cat.speak())
print("cow says:",cow.speak())
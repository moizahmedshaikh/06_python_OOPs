# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.bread = breed

    def bark(self):
        print(f"{self.name} says: Woof Woof!")

d1 = Dog("Bruno", "German Shepherd")
d2 = Dog("Oreo", "Poodle")
d3 = Dog("Tyson", "Doberman")

d1.bark()
d2.bark()
d3.bark()
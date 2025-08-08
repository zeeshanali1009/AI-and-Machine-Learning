# Grandparent
class Animal:
    def eat(self):
        print("Animal eats food")

# Parent
class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

# Child
class Dog(Mammal):
    def bark(self):
        print("Dog barks")

# Example usage
dog = Dog()
dog.eat()   # From Animal
dog.walk()  # From Mammal
dog.bark()  # From Dog

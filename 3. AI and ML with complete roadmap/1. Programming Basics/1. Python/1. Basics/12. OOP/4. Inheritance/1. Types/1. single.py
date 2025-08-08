# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Example usage
dog = Dog()
dog.speak()  # Inherited from Animal
dog.bark()   # Defined in Dog

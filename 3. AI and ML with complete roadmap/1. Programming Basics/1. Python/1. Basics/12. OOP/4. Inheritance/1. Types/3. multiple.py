# First Parent
class CanFly:
    def fly(self):
        print("I can fly!")

# Second Parent
class CanSwim:
    def swim(self):
        print("I can swim!")

# Child class inherits from both
class Duck(CanFly, CanSwim):
    def sound(self):
        print("Quack!")

# Example usage
duck = Duck()
duck.fly()    # From CanFly
duck.swim()   # From CanSwim
duck.sound()  # From Duck

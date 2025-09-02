# inheritance is used for using the functions of one class into another using the inheritance 

class Animal:
    def sound (self):
        print(f"Animals make different sounds")

class Lion(Animal):
    def sound(self):
        print(f"Lion makes the furious sound!")

class Cat(Animal):
    def sound(self):
        print(f"Cat makes the little sound!")


animal =  Animal()
animal1 = Lion()
animal2 = Cat()
animal1.sound()
animal2.sound()
class Student:
    def set_details(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Creating an object of the class
student1 = Student()

# Setting details using the method
student1.set_details("Zeeshan Ali", 20, "Kasur")

# Accessing and printing the attribute
print(student1.name)

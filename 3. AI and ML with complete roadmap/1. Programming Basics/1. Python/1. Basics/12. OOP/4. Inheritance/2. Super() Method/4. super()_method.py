# in the method overriding
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call the parent version
        print("Dog barks")

dog = Dog()
dog.speak()

# in the constructor overriding
class Person:
    def __init__(self, name):
        self.name = name
        print("Person initialized")

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)  # Call parent constructor
        self.emp_id = emp_id
        print("Employee initialized")

emp = Employee("Alice", 101)
print(emp.name, emp.emp_id)

# Here we will be covering the basic concepts of OOP like:
# - class: a blueprint that defines the structure and behavior (attributes + methods) for its objects.
# - objects: instances of a class that can store data in attributes and use methods defined in the class.
# - attributes: variables inside a class that hold data specific to each object.
# - methods: functions defined inside a class that describe the behaviors of the objects.

class Student:
    # Class attributes (default values) — these can be overridden by object-specific values.
    name = ""
    address = ""
    roll_no = ""

    # Constructor:
    # The __init__ method is a special method in Python classes that runs automatically 
    # when you create a new object from the class.
    # It is mainly used to initialize object attributes.

    # Default constructor (no parameters except 'self') — this will be overridden by the parameterized one below.
    # def __init__(self):
    #     print("I am the default constructor!")  # Executes when object is created without parameters.

    # Parameterized constructor — used when we pass arguments while creating the object.
    # 'self' refers to the current object being created, allowing access to its attributes and methods.
    def __init__(self, name, address, roll_no):
        self.name = name        # Assigning values to object attributes.
        self.address = address
        self.roll_no = roll_no

    # Methods in a class can be:
    # - Instance methods (require 'self')
    # - Class methods (@classmethod)
    # - Static methods (@staticmethod)

    # Example of a static method:
    # @staticmethod
    # def greet():  # Static methods do not take 'self' and cannot access instance attributes directly.
    #     print("Hello!")  

    # Instance method — requires 'self' so it can access the object's attributes.
    def greet(self, extra_message):
        # Using f-string for formatted output.
        print(f"Hello, {self.name}! {extra_message}")

# Creating object using parameterized constructor.
s2 = Student("Zeeshan", "KRK", "121212")

# Calling the greet method with an additional message.
s2.greet("Welcome to the OOP world!")

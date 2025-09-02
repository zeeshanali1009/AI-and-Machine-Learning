class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Copy constructor
    def copy(self, other_student):
        self.name = other_student.name
        self.age = other_student.age

student1 = Student("Zeeshan", 20)
student2 = Student("", 0)
student2.copy(student1)

print(student2.name)  

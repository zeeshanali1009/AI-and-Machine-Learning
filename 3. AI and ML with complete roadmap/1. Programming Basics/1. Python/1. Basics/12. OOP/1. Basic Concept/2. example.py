class Student:
    def __init__(self, name, marks):
        self.name  = name 
        self.marks = marks
    
    def avg_marks(self):
        total = 0 
        for val in self.marks:
            total += val
        average = total / len(self.marks)   # calculate average
        print("Hi", self.name, "Your average marks are:", average)


s1  = Student("Zeeshan", [56, 67, 78, 78])
s1.avg_marks()

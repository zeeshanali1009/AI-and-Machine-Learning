# class Student:
#     def __init__(self, eng,urdu,math):
#         self.eng = eng
#         self.urdu = urdu
#         self.math = math
#         self.percentage  = str((self.eng+ self.urdu + self.math)/3)
    

# std1  = Student(78,78,78)
# print(std1.percentage) 
# but if we change the math number the percentage must also chage but it does not gets chaged
# std1.math = 89
# print(std1.percentage) 
# so this problem can be solved by :
# class Student:
#     def __init__(self, eng, urdu, math):
#         self.eng = eng
#         self.urdu = urdu
#         self.math = math
#         self.percentage = 0

#     def calpercentage(self):
#         self.percentage = (self.eng + self.urdu + self.math) / 3

# std1 = Student(78, 78, 78)
# std1.calpercentage()
# print(std1.percentage)  # 78.0

# std1.math = 89
# std1.calpercentage()
# print(std1.percentage)  # 81.666...

class Student:
    def __init__(self, eng, urdu, math):
        self.eng = eng
        self.urdu = urdu
        self.math = math

    @property
    def percentage(self):
        return (self.eng + self.urdu + self.math) / 3

std1 = Student(78, 78, 78)
print(std1.percentage)  # 78.0

# Update marks
std1.math = 89
print(std1.percentage)  # 81.666...





    
        
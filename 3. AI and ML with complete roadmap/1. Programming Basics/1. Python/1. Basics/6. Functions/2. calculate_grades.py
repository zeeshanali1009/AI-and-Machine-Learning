# now we have the problem like we have the marks of the students in the form of lists
# we have to find the average and also we have to calculate the grades of the students as well

marks = [12, 4, 45, 56, 76, 77, 24, 76, 67, 79, 9, 45, 79]

# calculating the average marks
def average_marks(marks):
    sum_of_marks  = sum(marks)
    number_of_students = len(marks)
    average_marks = sum_of_marks / number_of_students
    return average_marks

# calculating the grades as well
def calculate_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = "B"
    elif average_marks >= 50:
        grade = "C"
    else:
        grade = 'F'
    
    return grade

average = average_marks(marks)
grades = calculate_grade(average)

print(f"Your average marks are: {average}")
print(f"Your grades are: {grades}")

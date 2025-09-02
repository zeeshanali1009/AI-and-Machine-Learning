# third method is the list comprehension method 

sqaures_1 =()
sqaures_1 = [i**2 for i in range(1,11)]
print(sqaures_1)
#  we can also make another condition into it like 
sqaures_1 =()
sqaures_1 = [i**2 for i in range(1,11) if i % 2 ==0]
print(sqaures_1)
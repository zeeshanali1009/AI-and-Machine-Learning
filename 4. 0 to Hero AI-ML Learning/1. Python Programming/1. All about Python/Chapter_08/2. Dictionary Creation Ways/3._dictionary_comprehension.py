# third method is the list comprehension method 

sqaures ={}
sqaures =  {i: i*i for i in range(1,11)} 

print(sqaures)
#  we can also make another condition into it like 
sqaures =()
sqaures = {i: i*i for i in range(1,11) if i % 2 ==0}
print(sqaures)
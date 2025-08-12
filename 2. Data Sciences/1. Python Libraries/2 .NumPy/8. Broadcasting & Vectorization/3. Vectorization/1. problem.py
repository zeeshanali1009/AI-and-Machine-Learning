list1 = [12,23,23]
list2 = [45,56,67]

result  = [x+y for x,y in zip(list1,list2)]
print(result)
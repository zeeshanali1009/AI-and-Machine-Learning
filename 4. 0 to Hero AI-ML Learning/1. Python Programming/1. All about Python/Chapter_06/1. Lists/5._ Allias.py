# Allias is like,suppose you have two lists and you are assigning the list one content to the second list 
# in this way if you are changing the list one content the content of the second list will also be changed
# because they are pointing at the same memory location

list_1 = [1,23,34,4,"Zeeshan"]
list_2 = list_1
print(list_1, list_2)

list_1[0] ="Ali Raza"
print(list_1, list_2)

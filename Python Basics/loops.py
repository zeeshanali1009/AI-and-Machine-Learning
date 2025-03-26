# range represents the last index number for the loop
# identation matters very much as the following block of code is properly identated
for i in range(10):
    print("Hello World")
    print("Hello Pakistan")
# this block of code is not properly identated
for i in range(10):
    print("Hello World")
print("Hello Pakistan")
# printing the list
mylist = [10,20,30,40,50,60,70,80]
for i in mylist:
 print(i)
# loop in list
mylist = [10,20,30,40,50,60,70,80]
for i in range(len(mylist)):
 print(i,mylist[i])
# loop in the dictionary
thisdirectory ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1986
}
#built in function to get the keys of the directory
for key in thisdirectory.keys():
   print(key)
# built in function to get the values of the keys
for value in thisdirectory.values():
   print(key)
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


def myfunc(funcparameter):
   for i in funcparameter:
      print(i)

thislist = [12,13,14,15]
myfunc(thislist)

# looping through string
for x in "Apple":
   print(x)

# range function further specs
numbers = [12,12,12,12,12]

for i in range(0,5):
    print(numbers[i])


# finding the even numbers 
numbers = [0,2,4,6,8,10]
print("Even numbers are ")
for i in numbers:
   if i % 2 ==0:      
      print(" ", i)

# while loop
# example 01
number =1
while number < 60:
   print(number)
   number = number +1

#    example #02
count = 0
while count <3 :
    print("count is ", count)
    count = count +1

# example 03
password = ""
while password !="secret":
   password = input("Enter the password")
if password == "secret":
      print("Login Successfull")
else:
      print("Login is not successfull")

# program to sum of first 10 numbers
total = 0
num =1
while num <=10:
    total = total + num
    num = num +1
print ("total sum is = ", total)

# program to check the number of letter in the word
def count(string):
   words = string.split()
   return len(words)

sentence = "Pakistan is an islamic country"
word_count = count(sentence)
print ("Number of words are ", word_count)

   
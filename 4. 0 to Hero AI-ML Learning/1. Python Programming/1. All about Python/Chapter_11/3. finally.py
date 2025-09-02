try:
    file = open("C:\Users\Zeeshan Ali\Desktop\Progress-towards-Python\2nd_Step to Python\Chapter_11\1. intro.txt")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file has not been found!")

finally:
    file.close()
    print("Operations has been completed successfuly!")
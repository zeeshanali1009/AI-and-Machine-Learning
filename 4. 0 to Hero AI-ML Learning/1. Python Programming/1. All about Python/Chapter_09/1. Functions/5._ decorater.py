# decorater is one of the most important concept of the python programming like we can change the
#  function inside the function without changing the main function code 

def my_decorator(func):
    def wrapper():
        print("Something is happening out here before the function.")
        func()
        print("Something is happening out here after the function.")
    return wrapper  # Return the function, not the result of calling it

@my_decorator
def greet():
    print("Hello!")

greet()

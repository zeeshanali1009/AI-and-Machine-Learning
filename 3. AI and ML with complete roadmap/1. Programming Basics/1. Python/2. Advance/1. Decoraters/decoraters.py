
# Decorator function
# def greet(fx):
#     def mfx():
#         print("This is the start.")  # before calling the original function
#         fx()                         # call original function
#         print("This is the end.")    # after calling the original function
#     return mfx                      # return the wrapper function


# for the parameterized functions it would be like 
#  Decorator function
def greet(fx):
    def mfx(*arg, **kwargs):
        print("This is the start.")  
        result = fx(*arg, **kwargs)                         
        print("This is the end.") 
        return result   
    return mfx                      
# Using decorator syntax
# @greet
# def hlo():
#     print("Hello!")

# Basic function
@greet
def add(a, b):
    return a + b

# Call the decorated function
# hlo()
res = add(12,12)
print("Result = ",)

# Or call decorator manually
# greet(hlo)()

import time
import multiprocessing

# Multiprocessing allows a program to run multiple processes in parallel,
# each with its own Python interpreter and memory space.
# It bypasses Python’s Global Interpreter Lock (GIL),
# making it ideal for CPU-bound tasks that need true parallelism.

# Using a Manager list to share data safely between processes
result =[]

def cal_square(numbers):
    # Calculate and print the square of each number
    for n in numbers:
        result.append(n * n)  
    print("Result array within the function:", str(result))

if __name__=="__main__":
    arr = [12, 23, 35, 45]


    p = multiprocessing.Process(target=cal_square, args=(arr,))

    p.start()  # Start the process

    p.join()   # Wait for the process to finish

# Print the shared result list from the main process
    print("Result outside process:", str(result))

# Note:
# Unlike threading, multiprocessing runs separate Python interpreters,
# so global variables are not shared unless managed explicitly (like using Manager()).

import time
import multiprocessing

# Multiprocessing allows a program to run multiple processes in parallel,
# each with its own Python interpreter and memory space.

# Using a Manager list to share data safely between processes
square_result = multiprocessing.Manager().list()

def cal_square(numbers):
    # Calculate and print the square of each number
    for n in numbers:
        print("Square:", n * n)
        square_result.append(n * n)  # Append result to shared list
    print("Result array within the function:", list(square_result))

arr = [12, 23, 35, 45]

# Create a Process object (note uppercase 'P') to run cal_square in a separate process
t1 = multiprocessing.Process(target=cal_square, args=(arr,))

t1.start()  # Start the process

t1.join()   # Wait for the process to finish

# Print the shared result list from the main process
print("Result outside process:", list(square_result))

# difference between the multithreading and dmulti processing
# muti processing means that the multi processes are being done in the differnt memory location
# multi threading means that the multiple threads are being created in the multi processes having the same memory addresses 
# like a power point opened , illustrator opened , chrome opened these are the multiprocessing 
# and the threads like the different tabs in teh same process represents the multithreading
# multi processes takes the huge memory while the multi threads takes the less memory




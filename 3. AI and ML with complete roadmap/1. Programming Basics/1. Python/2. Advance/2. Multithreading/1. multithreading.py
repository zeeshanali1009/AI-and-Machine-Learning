# Multithreading is an important concept used to minimize the time taken by the program for the execution process.
# Multithreading means that multiple tasks are being done in a parallel manner to save time and improve efficiency as well.
# Multithreading makes use of idle time of the CPU to improve efficiency.
# We will take an example to discuss more.

import time
import threading

def cal_square(numbers):
    print("The squares of each number are:")
    for n in numbers:
        time.sleep(0.2)  # Simulate time-consuming task
        print("Square:", n * n)
    
def cal_cubes(numbers):
    print("The cubes of each number are:")
    for n in numbers:
        time.sleep(0.2)  # Simulate time-consuming task
        print("Cube:", n * n * n)
    
arr = [12, 23, 35, 45]

# If we run these functions sequentially, it will take more time.
# Using threads, time taken will become less as both functions execute concurrently.

t1 = threading.Thread(target=cal_square, args=(arr,))
t2 = threading.Thread(target=cal_cubes, args=(arr,))

t1.start()
t2.start()

# wait for both threads to complete
t1.join()
t2.join()

# Note:
# Because of multithreading, output sequence is not guaranteed.
# When one function is in sleep mode, CPU switches to execute the other,
# which is why total time taken is less compared to sequential execution.

# multiprocessing pool usually created to divide the load of the function vusually so that the 
# function performs at the faster rate like it involves the concept of map and reduce 
# in the map the function resources will be distributed into the different cores of the cpu and then after the 
# execution these resources will be reduced to a single one.
import time
import multiprocessing

def f(n):
    total = 0
    for x in range(1000):
        total += x * x
    return total

if __name__ == "__main__":
    NUM_TASKS = 10000  # same for both

    # Parallel processing
    t1 = time.time()
    with multiprocessing.Pool() as p:
        result = p.map(f, range(NUM_TASKS))
    print("Pool Time:", time.time() - t1)

    # Serial processing
    t2 = time.time()
    result = []
    for x in range(NUM_TASKS):
        result.append(f(x))
    print("Serial Processing took:", time.time() - t2)

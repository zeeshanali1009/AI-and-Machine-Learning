# As we have seen earlier that the processes shares the different memory locations.
# as we seen in the previous problem same array was giving difffernt outputs so the problem can be resolved by the following solutions

import multiprocessing

def cal_square(numbers, result, v):
    v.value = 5.67  # Update shared Value
    for idx, n in enumerate(numbers):
        result[idx] = n * n  # Store squares in shared Array

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    
    # Create shared Array of size 4 (must match numbers length)
    result = multiprocessing.Array("i", len(numbers))
    
    # Create shared Value (float)
    v = multiprocessing.Value("d", 0.0)  # "d" means double precision float
    
    # Create and start process
    p = multiprocessing.Process(target=cal_square, args=(numbers, result, v))
    p.start()
    p.join()
    
    # Print shared results
    print("Squares:", list(result))
    print("Shared value v:", v.value)

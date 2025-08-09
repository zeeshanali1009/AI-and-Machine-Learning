# here the data resource are being shared in teh queue
import multiprocessing


def cal_square(numbers, q):
    # Calculate and print the square of each number
    for n in numbers:
        q.put(n * n)  


if __name__=="__main__":
    arr = [12, 23, 35, 45]


    q = multiprocessing.Queue()
    q = multiprocessing.Process(target=cal_square, args=(arr,))

    q.start()  # Start the process

    q.join()   # Wait for the process to finish


    while q.empty() is False:
        print(q.get())

# there are two queues 
# multiprocessing queue: this stores only the data of the multiprocesses at the same memory locations
# queue : this queuee just stores the data of the threads at the same memory locations
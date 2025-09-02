# generaters are like the slow iteraters they iterates through a particular range with a specific condition 

def count_down(num):
    while num > 0:
        yield num
        num -= 1

for number in count_down(5):
    print(number)

import random


def average(d,n):
    avg = d/n
    return avg


def running_average(numbers):
    avgs = []
    total = 0
    for i, num in enumerate(numbers):
        total += num
        current_avg = average(total, i+1)
        avgs.append(current_avg)
   
    return avgs

def highest_running_average(numbers):
    avgs = running_average(numbers)
    highest = max(avgs)
    return highest

def generate_numbers(n):
    return random.sample(range(1, 1000), n)

def generate_numbers_with_zero(n):
    return random.sample(range(0, 9), n)

if __name__ == '__main__':
    numbers = generate_numbers(100)
    print("Numbers: ", numbers)
    print("Running average: ", running_average(numbers))
    print("Highest running average: ", highest_running_average(numbers))

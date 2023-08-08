

from example import generate_numbers, generate_numbers_with_zero, highest_running_average, running_average


def math_stuff(numbers):
    total = 0
    for num in numbers:
        total += num
        moreStuff = total / num
    return moreStuff

if __name__ == '__main__':
    # Use this as an example for the call stack, as it jumps between example.py and example2.py
    # numbers = generate_numbers(100)
    # print("Numbers: ", numbers)
    # print("Running average: ", running_average(numbers))
    # print("Highest running average: ", highest_running_average(numbers))

    # Use this to see the variables on the left hand side, that show why the error gets thrown. Hint! What cant you divide by?
    numbers = generate_numbers_with_zero(5)
    result = math_stuff(numbers)
    print("The average is:", result)

  




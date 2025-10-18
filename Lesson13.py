# Keyword Arguments in Python

def timepass(number, by):
    return number + by


print(timepass(1, by=3))

# Default Arguments in Python


def timepass1(number, by=1):
    return number + by


print(timepass1(5))

# More Arguments


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply(2, 4, 10))

# Functions in Python

def callout():
    print("This is a function callout")
    print("Functions help organize code into reusable blocks")
    print("They can take inputs and return outputs")


callout()


# Function Parameters and Arguments in Python

def callout(first, last):
    print("This is a function callout")
    print(f"Hello {first} {last}")


callout("John", "Doe")

# Types of Functions in Python
# 1. Perfrorming a task function
# 2. Returning a value function


def get_name(first):
    return f"Hi {first}"


message = get_name("Puneet")
file = open("Lesson13.py", "w")
file.write(message)
file.close()

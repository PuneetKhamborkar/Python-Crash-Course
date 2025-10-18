# For loops in Python

# Print odd numbers between 1 and 100
for number in range(1, 10, 3):  # Always end for statement with a colon
    print("random numbers", number, number * ".")

# For Else Loops in Python

successful = True

for number in range(3):
    print("Attempt", number + 1)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

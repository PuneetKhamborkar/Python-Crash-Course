# While loops in Python

# name = ""
# while name.lower() != "quit":  # Always end while statement with a colon
#    name = input(">")
#    print("ECHO", name)

# Infinite Loops in Python

while True:
    name = input(">")
    print("ECHO", name)
    if name.lower() == "quit":
        break

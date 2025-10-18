# Conditional Statements in Python

pencil = 15

if pencil < 10:  # Always end if statement with a colon
    print("loss")
elif pencil > 10:  # Always end elif statement with a colon
    print("profit")
else:
    print("no profit no loss")


# Ternary Operators in Python

pencil = 12
message = "profit" if pencil > 15 else "loss"
print(message)


# Logical Operators in Python
# and or not

high_income = True
good_credit = True
unemployeed = False

if high_income and good_credit and not unemployeed:  # Short-circuit evaluation
    print("Eligible for loan")

# if high_income or good_credit:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

message = "Eligible for loan" if high_income and good_credit and not unemployeed else "Not eligible for loan"
print(message)

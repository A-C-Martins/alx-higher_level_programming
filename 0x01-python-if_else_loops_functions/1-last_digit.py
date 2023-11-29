#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
ldigit = repr(number)[-1]
if int(ldigit) > 5:
    print(f"last digit of {number} is {ldigit} and is greater than 5")
elif int(ldigit) == 0:
    print(f"last digit of {number} is {ldigit} and is 0")
else:
    print(f"last digit of {number} is {ldigit} and is less than 6 and not 0")

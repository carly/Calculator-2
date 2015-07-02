"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True: 
    entry = raw_input("> ")
    entry_new = entry.lstrip()
    tokens = entry_new.split(" ")

    operator = tokens[0]
    num1 = int(tokens[1])
    
    if len(tokens) > 2:
        num2 = int(tokens[2])
    else:
        num2 = None    


    if operator == "q":
        file.close()

    elif operator == "+":
        print add(num1, num2)

    elif operator == "-":
        print subtract(num1, num2)

    elif operator == "*":
        print multiply(num1, num2)

    elif operator == "/":
        print divide(num1, num2)

    elif operator == "square":
        print square(num1)

    elif operator == "cube":
        print cube(num1)

    elif operator == "pow":
        print power(num1, num2)

    elif operator == "mod":
        print mod(num1, num2)

    else: 
        print "Invalid entry. Try again."






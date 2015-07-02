"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

operator_dict = {"+": add,
                 "-": subtract, 
                 "*": multiply,
                 "/": divide,
                 "square": square,
                 "cube": cube,
                 "pow": power,
                 "mod": mod}

# Your code goes here
while True: 
    entry = raw_input("> ")
    entry_new = entry.lstrip()
    tokens = entry_new.split(" ")

    operator = tokens[0]

    if len(tokens) < 2 and operator == "q":
        break
    elif operator not in operator_dict: 
        print "Invalid entry. Try again."

    if len(tokens) < 3: 
        num1 = int(tokens[1])
        opperands = "num1"

    if len(tokens) > 2:
        num2 = int(tokens[2])
    else:
        num2 = None    

    



    print operator_dict[operator]()
    

    if 






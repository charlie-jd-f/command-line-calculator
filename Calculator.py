# This is a command line calculator

print('''Welcome!
This is a command-line calculator which performs simple calculations such as:
Addition (+), Subtraction (-), Multiplication (*), Division (/).

To use the calculator, input in the format:
<number> <operation> <number> e.g. 1 / 2

To exit, type "Exit" \n''')

while True:

    user_input = (input("Enter your calculation below: \n")).lower()
    calc_info = user_input.split(" ")


    if user_input == "exit":
        break

    # Checks that user has input the calculation in the correct format
    elif len(calc_info) != 3:
        print("Format Error: Please insert a space between operations")
    
    else:

        if '+' in calc_info:
            
            # Add the two values, print error if user has not input numbers

            try:
                a = float(calc_info[0])
                b = float(calc_info[2])
                value = a + b
                print(value)

            except ValueError:
                print("Input Error: Ensure you input numbers to calculate")

        elif '-' in calc_info:
            
            # Subtract the two values, print error if the user has not
            # input numbers

            try:
                a = float(calc_info[0])
                b = float(calc_info[2])
                value = a - b
                print(value)
            
            except ValueError:
                print("Input Error: Ensure you input numbers to calculate")
        
        elif '*' in calc_info:
            
            # Multiply the two values, print error if the user has not
            # input numbers

            try:
                a = float(calc_info[0])
                b = float(calc_info[2])
                value = a * b
                print(value)
            
            except ValueError:
                print("Input Error: Ensure you input numbers to calculate")
        
        elif '/' in calc_info:
            
            # Divide the two values, print error if the user has not input
            # numbers, or if there is a divide by zero error

            try:
                a = float(calc_info[0])
                b = float(calc_info[2])
                value = a/b
                print(value)

            except ValueError:
                print("Input Error: Ensure you input numbers to calculate")
            except ZeroDivisionError:
                print("Arithmatic Error: You cannot divide by 0")

        else:
            print("Format Error: You have not included an operation")

# Next steps - improve to add more functionality such as "5 * 1 + 3"
while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")
    
    if user_input == 'quit':
        break
    elif user_input == 'add':
        print('x+y=?')
        x = int(input("Enter first number (x): "))
        y = int(input("Enter second numer (y): "))
        z = x+y
        print(f'x+y={z}')
    elif user_input == 'subtract':
        print('x-y=?')
        x = int(input("Enter first number (x): "))
        y = int(input("Enter second numer (y): "))
        z = x-y
        print(f'x-y={z}')
    elif user_input == 'multiply':
        print('x*y=?')
        x = int(input("Enter first number (x): "))
        y = int(input("Enter second numer (y): "))
        z = x*y
        print(f'x*y={z}')
    elif user_input == 'divide':
        print('x/y=?')
        x = int(input("Enter first number (x): "))
        y = int(input("Enter second numer (y): "))
        z = x/y
        print(f'x/y={z}')
    else:
        print('Wrong option!')
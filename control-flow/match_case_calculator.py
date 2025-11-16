# Ask user to enter two numbers 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


# Ask user the operation to perform
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The results is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1/num2
            print(f"The result is {result}")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation. Please choose from +, -, *, /.") 

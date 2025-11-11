# Ask user to enter number for multiplication table
number = int(input("Enter a number to see its multiplication table:"))

# Generate and Print the Multiplication Table
for num in range(1, 11):
    product = number * num
    print(f"{number} * {num} = {product}") 


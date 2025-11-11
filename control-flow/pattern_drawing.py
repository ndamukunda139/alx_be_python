# ask user to enter size of the pattern
size = int(input("Enter the size of the pattern: "))
count = size
# Draw the pattern
while size > 0:
    for i in range(count):
        print("*", end=" ")
    print()
    size -= 1
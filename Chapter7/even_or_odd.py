"""Ask for non negative integer and find if it is even or odd."""

number = input("Enter the number, let's see if it is even or odd: ")

if int(number) % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

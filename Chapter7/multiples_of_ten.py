"""
Ask the user for a number, and then report whether the number is a multiple of 10 or not.
"""
num1 = input("Enter non negative integer: ")
num1 = int(num1)

if num1%10 == 0:
    print(f"{num1} is multiple of 10.")
else:
    print(f"{num1} is not multiple of 10!")
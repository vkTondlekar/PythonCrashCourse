"""
Consider a program that determines whether people are tall enough to ride a roller coaster.
"""
height = input("How tall you are? please enter in cm: ")

height = int(height)

if height >= 120:
    print("\n Enjoy your ride.")
else:
    print("\n We can't permit to board on ride.")

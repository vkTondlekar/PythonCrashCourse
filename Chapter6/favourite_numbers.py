"""
Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name
and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
"""
favourite_number = {'alpha': 99,
                    'Beta': 563,
                    'Gamma': -4,
                    'lambda': 5349,
                    'theta': 93232232}
for number in favourite_number:
    print(number.capitalize(), " favourite number is", favourite_number[number])

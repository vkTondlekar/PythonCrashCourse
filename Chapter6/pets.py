"""
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind
of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and
as you do, print everything you know about each pet.
"""
chloe = {'animal':'cat',
         'owner':'adam',
         'color':'sky blue'}
mel = {'animal':'dog',
       'owner':'michael',
       'color':'brown'}
snowball = {'animal':'rabbit',
            'owner':'duke',
            'color':'white'}
pets = [chloe, mel, snowball]

for pet in pets:
    print(pet)
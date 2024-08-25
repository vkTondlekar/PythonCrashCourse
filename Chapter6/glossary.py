"""
Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion,
let’s call it a glossary.
Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in
your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and
then its meaning, or print the word on one line and then print its meaning indented on a second line.
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""
glossary = {'insert': 'The method inserts the specified value at the specified position.',
            'get': 'The method returns the value of the item with the specified key.',
            'remove': 'The method removes the specified item.',
            'strings': 'Strings in python are surrounded by either single quotation marks, or double quotation marks.',
            'boolean': 'Booleans represent one of two values: True or False.'
            }
#print(glossary['insert'])
for item in glossary:
    print(item,":",glossary[item])

for key in glossary:
    print(key,"\n",glossary[key])

for key, value in glossary.items():
    print("\n",key,":",value)
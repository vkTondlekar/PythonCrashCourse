"""
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99)
by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should automatically be included in the output.
"""
glossary = {'insert': 'The method inserts the specified value at the specified position.',
            'get': 'The method returns the value of the item with the specified key.',
            'remove': 'The method removes the specified item.',
            'strings': 'Strings in python are surrounded by either single quotation marks, or double quotation marks.',
            'boolean': 'Booleans represent one of two values: True or False.',
            'sets':'Sets are used to store multiple items in a single variable.',
            'whileLoop':'With the while loop we can execute a set of statements as long as a condition is true.'
            }

for key in glossary.keys():
    print(key,":",glossary[key])
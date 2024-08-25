"""
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair
might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
Use a loop to print the name of each river included in the dictionary.
Use a loop to print the name of each country included in the dictionary
"""

rivers = {'krishna':'india',
          'thames':'england',
          'amazon':'peru'}
for river in rivers.keys():
    print(f"{river.title()}, starts from {rivers[river]}")
for river in rivers.keys():
    print(f"\t {river.title()}")
for river in rivers.values():
    print(f"\t\t {river.title()}")
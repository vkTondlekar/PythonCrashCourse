"""
Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people,
and store all three dictionaries in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.
Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city
in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information
stored in your dictionary.
"""

person1 = {'first_name': 'Srinivasa',
           'last_name': 'Ramanujan',
           'age': 27,
           'city': 'Birmingham'
           }

person2 = {'first_name': 'Subhashchandra',
           'last_name': 'Bose',
           'age': 40,
           'city': 'Bengal'
           }

person3 = {'first_name': 'Albert',
           'last_name': 'Einstein',
           'age': 56,
           'city': 'Princetown'
           }
people = [person1, person2, person3]

for person in people:
    print(person)

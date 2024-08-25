"""
6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age,
and the city in which they live. You should have keys such as first_name, last_name, age, and city.
Print each piece of information stored in your dictionary.
"""
person = {'first_name':'Srinivasa',
          'last_name':'Ramanujan',
          'age':27,
          'city':'Birmingham'
          }
print("First name of person is:", person['first_name'],".")
print("And last name of person is:", person['last_name'],".")
print("Age of ", person['first_name'],"was", person['age'],".")
print("Mr.", person['last_name'], "used to live in", person['city'],"!")
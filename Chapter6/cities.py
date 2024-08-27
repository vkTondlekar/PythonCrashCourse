"""
Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of
information about each city and include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print
the name of each city and all the information you have stored about it.
"""
# Using the names of three cities as keys
cities = {'madurai': {'country': 'india',
                      'population': str(3345848),
                      'Marvel': 'Meenakshi Temple'},

          'paris': {'country': 'france',
                    'population': str(1277000),
                    'Marvel': 'Eifel tower'},

          'brasilia': {'country': 'brazil',
                       'population': str(4935000),
                       'Marvel': 'Airplane city'}
          }

for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    Marvel = city_info['Marvel']

    print(f"{city.title()}, is in {country.upper()} with population of {population} and {Marvel.title()} is a speciality.")


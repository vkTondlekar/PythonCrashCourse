"""
Write a function called describe_city() that accepts the name of a city and its country.
The function should print a simple sentence, such as Reykjavik is in Iceland.
Give the parameter for the country a default value. Call your function for three different cities,
at least one of which is not in the default country.
"""
from Chapter6.cities import country


def describe_city(city, country='Japan'):
    print(f"{city.capitalize()} is in a {country.capitalize()}")


describe_city('tokyo')

describe_city('Reykjavik', country='finland')

describe_city(country='sweden', city='stockholm')
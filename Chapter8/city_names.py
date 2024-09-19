"""
Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values that are returned.
"""
def city_country(city, country):
    fullname = f"{city.capitalize()}, {country.capitalize()}"
    return fullname

cities= city_country('mumbai','india')
print(cities)

cities= city_country('changi','singapore')
print(cities)

cities= city_country('barcelona','spain')
print(cities)
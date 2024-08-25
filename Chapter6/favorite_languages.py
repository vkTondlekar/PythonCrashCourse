"""
1.Tell Python to pull all the keys from the dictionary favorite_languages and assign them
one at a time to the variable name. Show the names of everyone who took the poll
2.Make another list of couple of friends.If their name is in the list friends.
Print a message, I see you love favorite_language!
3.use the keys() method to find out if a particular person was polled. This time, let’s find out if Erin took the poll
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
friends = ['jen', 'edward']

for name in sorted(favorite_languages.keys()):
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name]
        print(f"\t {name.title()}, I see you love {language}.")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll.")

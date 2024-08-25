"""
Use the code in favorite_languages.py (page 96).

Make a list of people who should take the favorite languages poll. Include some names that are already in the
dictionary and some that are not.
Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking
them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(f"{name.title()}'s favourite language is {favorite_languages[name]}.")

engineers = ['jen', 'christian', 'sarah', 'edward', 'clark', 'phil']

for engineer in engineers:
    if engineer in favorite_languages.keys():
        print(f"\t{engineer.title()}, thank you for you poll.")
    else:
        print(f"\t\t{engineer.title()}, kindly take our favorite_languages poll!")

# toppings
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# magic_number

answer = 17
if answer != 42:
    print('\nThat is not the correct answer. Please try again!')

# banned_users

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

car = 'audi'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(number, 'x', i, '=', number * i)
    i += 1
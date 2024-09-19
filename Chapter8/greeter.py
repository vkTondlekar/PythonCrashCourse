

def get_formatted_name(first_name, last_name, age=None):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name: ")
    print("Enter 'quit' to quit anytime!")

    f_name = input("First name: ")
    if f_name.casefold() == 'quit':
        break

    l_name = input("Last name: ")
    if l_name.casefold() == 'quit':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello {formatted_name.title()}!")

get_formatted_name('thomas', 'edison')
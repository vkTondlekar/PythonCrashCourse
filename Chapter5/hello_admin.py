"""
Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that
will print a greeting to each user after they log in to a website. Loop through the list, and
print a greeting to each user.
If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
If the list is empty, print the message We need to find some users!
"""
usernames = ['jim', 'neil', 'admin', 'vishal', 'nilesh', 'prashant', ]
#usernames = []
if not usernames:
    print("\nWe need to find some users!")
for username in usernames:
    if username == 'admin':
        print(f"\nHello admin, would you like to see a status report?")
    else:
        print("Hello " + username.title() + ", thank you for logging in again.")


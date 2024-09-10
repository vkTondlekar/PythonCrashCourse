"""
Consider a list of newly registered but unverified users of a website. After we verify these users,
how can we move them to a separate list of confirmed users? One way would be to use a while loop to
pull users from the list of unconfirmed users as we verify them and then add them to a separate list
of confirmed users
"""
#We begin with a list of unconfirmed users
unverified_users = ['robin', 'batman', 'bane', 'joker']
#an empty list to hold confirmed users
verified_users = []

#The while loop runs as long as the list unconfirmed_users is not empty
while unverified_users:
    current_user = unverified_users.pop()
#Within this loop, the pop() method removes unverified users one at a time from the end of unconfirmed_users
#joker will be the first name removed and assigned to current user and added to the verified_users list
    print(f"Verifying user: {current_user.title()}.........")
    verified_users.append(current_user)

print(f"\n The following users are confirmed:\n")
for verified_user in verified_users:
    print(verified_user.title())
#When the list of unconfirmed users is empty, the loop stops and the list of confirmed users is printed
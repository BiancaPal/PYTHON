# USING A LOOP WITH LISTS AND DICTIONARIES
# To modify a list as you work through it, use a while loop.

# MOVING ITEMS FROM ONE LIST TO ANOTHER

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
  current_user = unconfirmed_users.pop()

  print(f"Verifying user. {current_user.title()}")
  confirmed_users.append(current_user)

# In this example we popped the last index of unconfirmed_user, and place it into
# a variable which will later on be appended in the initiated confirmed_users lists.

# Displaying all the confirmed users.
print("The following users have been confirmed: ")
for confirmed_user in confirmed_users:
  print(confirmed_user.title())

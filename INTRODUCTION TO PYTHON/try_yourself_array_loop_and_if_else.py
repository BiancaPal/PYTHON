# Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print
# a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
# If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

usernames = ['Bianca', 'Alex', 'Eliza', 'Dario', 'admin']

for username in usernames:
  if username == 'admin':
    print(f" Hello {username}, would you like to see a status report?")
  else:
    print(f" Hello {username}, thank you for logging in ain")

# Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed.
print("\n")

usernames = []

if usernames:
  for username in usernames:
    if username == 'admin':
      print(f" Hello {username}, would you like to see a status report?")
    else:
      print(f" Hello {username}, thank you for logging in again")
else:
  print("We need to find some users!")

# Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the
# current_users list.
# Loop through the new_users list to see if each new username has already been used. If it has, print a message 
# that the person will need to enter a new username. If a username has not been used, print a message saying that
# the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do 
# this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
print("\n")

current_users = ['Bianca', 'Alex', 'Dario', 'Eliza', 'Leonidas']
current_users_lower = [current_user.lower() for current_user in current_users]



new_users = ['Dario', 'Nicolas', 'Beronica', 'Eliza', 'Toto']

for new_user in new_users:
  if new_user.lower() in current_users_lower:
    print(f"The username {new_user} has already been used")
  else:
    print(f"The username {new_user} is available!")

# Store the numbers 1 through 9 in a list
# Loop through the list
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output
# should read "1st 2nd 3rd 4th fth 6th 7th 8th 9th", and each result should be in a separate line.

print("\n")

for number in range(1,10):
  if number == 1:
    print(f"{number}st")
  elif number == 2:
    print(f"{number}nd")
  elif number == 3:
    print(f"{number}rd")
  else:
    print(f"{number}th")
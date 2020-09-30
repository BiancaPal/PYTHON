# You'll often find it useful to pass a list to a function, whether it's a list of names,
# numbers, or more complex objects, such as dictionaries. When you pass a list to a function
# the function gets direct access to the contents of the list. Let's use functions to make 
# working with lists more efficient.

# Say you have a list of users and want to print a greeting to each. The following example 
# sends a list of names to a function called greet_users(), which greets each person in the
# list individually:


def greet_users(names):
  """Print a simple greeting to each user in the list"""
  for name in names:
    msg = f"Hello, {name.title()}!"
    print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

# In the calling we used usernames as the argument, that later on the function loops through
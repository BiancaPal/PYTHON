# A DICTIONARY IN A DICTIONARY

# You should not nest list and dictionaries too deeply. If you're nesting items much deeper
# than what you see in the preceeding examples or you're working with someone else's code 
# with significant levels of nesting, most likely a simpler wat to solve the problem exists.

users = {
  'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'United stated',
    },
  
  'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'Polony',
    },
  }

for username, user_info in users.items():
  print(f"\nUsername: {username}")
  full_name = f"{user_info['first']} {user_info['last']}"
  location = user_info['location']
  
  print(f"\tFull name: {full_name.title()}")
  print(f"\tLocation: {location.title()}")

# We first define a dictionary called users with two keys: one each for the usernames. The 
# value associated with each key is a dictionary that includes each other user's properties.
# We loop through the users dictionaries with method items(). Python assigns the key to the
# variable username and the dictionary associated is assigned to the variable user_info.
# The dictionary user_info has 3 keys 'first' 'last' 'location'. We use each key to generate
# a neatly formatted full name and location for each person, and then print a summary of what
# we know about each user.

# Notice that the structure of each user's dictionary is identical. Although not required 
# by Python, this structure makes nested dictionaries easier to work with. If each user's 
# dictionary had different keys, the code inside the for loop would be more complicated.

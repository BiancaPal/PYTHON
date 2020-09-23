# NESTING
# Sometimes you'll want to store multiple dictionaries in a list, or a list of items as a 
# value in a dictionary. This is call nesting. You can nest dictionaries inside a list of 
# items inside a dictionary, or even a dictionary inside another dictionary. Nesting is a 
# powerful feature, as the following examples will demonstrate.


# A LIST OF DICTIONARIES
# One way is to make a list of aliens in which each alien is a dictionary of information 
# about that alien.

alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
  print(alien)

# We first create 3 dictionaries, and then we store them in a list called aliens. And 
# finally we loop through it.

# In the following example we use range() to create a fleet of 30 aliens.
print("\n")
# Create an empty list for storing aliens.
aliens = []

# Make a 30 green aliens. Using the method range() in the foor loop, and appending them 
# into the empty aliens[] list.
for alien_number in range(30):
  new_alient = {'color':'green', 'points':5, 'speed':'slow'}
  aliens.append(new_alient)

# Show the first 5 aliens.
for alien in aliens[:5]:
  print(alien)
print("...")

# Show how many aliens have been created with the len() method.
print(f"Total number of aliens: {len(aliens)}")

# We will loop through a slice, that includes only the first 3 items. If the alien property
# color is 'green' we modify all the properties.
for alien in aliens[:3]:
  if alien['color'] == 'green':
      alien['color'] = 'yellow'
      alien['speed'] = 'medium'
      alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
  print(alien)
print("...")
  

# We will expand the loop by adding an elif block that turns yellow aliens into red, fast-
# moving ones worth 15 points each. Without showing the entire program again.

for alien in aliens[:3]:
  if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = '10'
  elif alien['color'] == 'yellow':
    alien['color'] = 'red'
    alien['speed'] = 'fast'
    alien['points'] = '15'


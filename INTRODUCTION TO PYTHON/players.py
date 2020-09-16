# You can also work with a specific group of items in a list, which Python calls a slice
# Python stops one item before the second index you specified, this is an example:

players = ['charles', 'martina', 'michae', 'florence', 'eli']
print(players[0:3])

# You can start the slice at whatever index you want, for example 1 and 4.
print(players[1:4])

# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list.
print(players[:4])

# The above can be the other way around too, when you omit the last index, it will go through the end of the list
print(players[2:])

# You can also print the last "X" values before the last index
print(players[-3:])

# You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.
print(players[0::2])

# LOOPING THROUGH A SLICE
# You can loop through a subset of the elements in a list. 

print("Here are the first three players on my team")
for player in players[:3]:
  print(player.title())


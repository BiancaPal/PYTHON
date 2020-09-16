
locations = ['Mykonos', 'Malta', 'Munich', 'Croatia']

# Print the list random, as in it's original order
print(locations)

# Display the list sorted in alphabetical order 
print(sorted(locations))

# Show that your list is still in it's original order
print(locations)

# Display the list sorted in reverse alphabetical order
print(sorted(locations,reverse=True))

# Show that your list is still in it's original order
print(locations)

# Use reverse() to change the order permanently
locations.reverse()
print(locations)

# Use reverse() again back to its original order

locations.reverse()
print(locations)

# Use sort() to change your list so it's stored in alphabetical order

locations.sort()
print(locations)

# Use sort() to change your list so it's stored in reverse alphabetical order

locations.sort(reverse=True)
print(locations)



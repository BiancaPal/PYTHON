pizzas = ['quattro stagioni', 'quoattro formaggi', 'diavola', 'romana', 'prosciutto e funghi', 'capricciosa', 'calzone']

# Use a slice to print the first three items from that program's
print(f"The first three items in the list are: {pizzas[:3]}")

# Use a slice to print the three items from the middle of the list
print(f"The items from the middle of the list are:{pizzas[2:5]}")

# Use a slice to print the last three items in the list.
print(f"The last three items of the list are: {pizzas[-3:]}")

# Make a copy of the list pizzas, and call it friend_pizzas
friend_pizzas=pizzas[:]

# Add a different element to each of the lists
pizzas.append('kebab')
friend_pizzas.append('hawaian')

# Prove that you have different lists

print("My favorite pizzas are:")
for pizza in pizzas:
  print(f"\t{pizza}")

print("\n")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
  print(f"\t{pizza}")

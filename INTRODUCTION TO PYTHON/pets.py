# Say you have a list of pets with the value 'cat' repeated several times. To remove all 
# instances of that value, you can run a while loop until 'cat' is no longer in the list, 
# as shown here:

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
  pets.remove('cat')

print(pets)

# While the value is still inside the pets lists, remove it, else break the while loop
# Replace the series of print() calls with a loop that runs through the dictionary's keys
# and values.

person = {
  'first_name': 'Bianca',
  'last_name': 'Pal',
  'age': 21,
  'city': 'Lleida'
  }

for key, value in person.items():
  print(f"The {key} of the person is {value}")

# When you're sure your loop works, add five more Python terms to your glossary. When you run 
# the program these new words and meanings should automatically be included in the output.

person['eyes'] = 'blue'
person['height'] = 1.74
person['weight'] = 52
person['hair color'] = 'brown'
person ['hairstyle'] = 'pixie short'

for key, value in person.items():
  print(f"The {key} of the person is {value}")

# Make a dictionary containing three  major rivers and the country each river runs through.

print("\n")

rivers = {
  'nile': 'North East Africa',
  'amazon':'South America',
  'yangtze':'China',
  }

# Use a loop to print a sentence about each river, such as "The Nile runs through Egypt"
print("\n")

for key, value in rivers.items():
  print(f"River {key.title()}, runs through {value.title()}") 

# Use a loop to print the name of each river included in the dictionary.
print("\n")

for key in rivers.keys():
  print(key.title())

# Use a loop to print the name of each country included in the dictionary.
print("\n")

for value in rivers.values():
  print(value.title())

# Make a list of people who should take the favorite languages poll. Include some names 
# that are already in the dictionary and some that are not.


favorite_languages = {
  'jen':'python',
  'sarah':'c',
  'edward':'ruby',
  'phil':'python',
  }

persons= ['bianca','alex','phil']

# Loop throught the list of people who should take the poll. If they have already taken 
# the poll, print a message thanking them for responding. If they have not yet taken the 
# poll, print a message inviting them to take the poll.

for person in persons:
  if person in favorite_languages.keys():
    print(f"Thank you {person} for taking the poll.")
  else:
    print(f"I invite you {person} to take the poll!")


# LOOPING THROUGH ALL KEY-VALUE PAIRS
user_0 = {
  'username': 'efermi',
  'first': 'enrico',
  'last': 'fermi',
  }

for key, value in user_0.items():
  print(f"\nKey:{key}")
  print(f"Value:{value}")

# To write a for loop for a dictionary, you create names for the two variables that will hold 
# the key and value in each key-value pair. You can choose any names for these two variables.

for k,v in user_0.items():
  print(f"\nKey:{k}")
  print(f"Value:{v}")

# The method items(), returns a list of key-value pairs. The for loop then assigns each of these
# pairs to tht two variables provided. In the preceding example, we use the variables to print 
# each key.

favorite_languages = {
  'jen':'python',
  'sarah':'c',
  'edward':'ruby',
  'phil':'python',
  }

for name, language in favorite_languages.items():
  print(f"\nName:{name}")
  print(f"Favorite Language:{language}")

# LOOPING THROUGH THE KEYS IN A DICTIONARY
# The keys() method is useful when you don't need to work with all of the values in a dictionary
# .Let's loop through favorite_languages dictionary and print the names of everyone who took the 
# poll.
print("\n")

for name in favorite_languages.keys():
  print(f"{name.title()}")

# Looping through the keys is actually the default behaviour when looping through a dictionary, 
# so this code would have worked exactly the same if you wrote...
print("\n")

for name in favorite_languages:
  print(f"{name.title()}")

# You can choose to use the keys() method explicity if it makes your code easier to read, or you 
# can omit if if you wish.

# We'll loop through the names in the dictionary as we did previously, but when the name matches 
# one of our friends, we'll display a message about their favorite language.

print("\n")

favorite_languages = {
  'jen':'python',
  'sarah':'c',
  'edward':'ruby',
  'phil':'python',
  }

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
  print(f"Hi {name.title()}")

  if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}")

# We create a list with the names phil and sarah
# We loop through the keys of the favorite languages dictionaries, and  display by default
# their name, if the keys match any of the values inside of the list, make the language a 
# variable by accessing the dictionary and then display it all together.

# You can also use the keys() method to find out if a particular person was polled. This time
# , let's find out if Erin took the pool:

print("\n")

if 'erin' not in favorite_languages.keys():
  print(f"Erin, please take the poll!")
else:
  print(f"Everything is fine Erin!") 

# LOOPING THROUGH A DICTIONARY'S KEYS IN A PARTICULAR ORDER

print("\n")

for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll")

# LOOPING THROUGH ALL VALUES IN A DICTIONARY
# If you are priarily interested in the values that a dictionary contains, you can use values()
# method to return a list of values without any keys.

print("\n")

for language in favorite_languages.values():
  print(language.title())

# To see each language without repetition, we can use set, a set is a collection in which 
# each item must be unique.

print("\n")

for language in set(favorite_languages.values()):
  print(language.title())

# You can build a set directly using braces and separating the elements with commas: It's 
# easy to mistake sets for dictionaries because they're both wrapped in braces. When you 
# see braces but no key-value pairs, you're probably looking at a set. Unlike lists and
# dictionaries, sets do not retain items in any specific order.


languages = {'ruby','python','c'}

print(languages)


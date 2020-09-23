favorite_languages = {
  'jen':['python', 'ruby'],
  'sarah':['c'],
  'edward':['ruby', 'go'],
  'phil':['python', 'haskell'],
  }

for name, languages in favorite_languages.items():
  print(f"\n{name.title()}'s favorite languages are:'")
  for language in languages:
    print(f"\t{language.title()}")

# We looped with the method items() the keys, and array values, and indented the for loop 
# accessing the value loop.

# When we loop through the dictionary at, we use the variable name languages to hold each 
# value from the dictionary, because we know that each value will be a list. Inside the 
# main dictionary loop, we use another for loop, to run through each person's list of favorite
# languages.

print("\n")

for name, languages in favorite_languages.items():
  if len(languages) > 1:
    print(f"\n {name.title()}'s favorite languages are:'")
  else:
    print(f"\n {name.title()}'s favortie language is:'")
  
  for language in languages:
      print(f"\t {language.title()}")
  
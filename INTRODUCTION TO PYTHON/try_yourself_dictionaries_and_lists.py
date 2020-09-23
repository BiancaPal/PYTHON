# DICTIONARIES IN LISTS

# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

bianca99 = {
    'first_name': 'Bianca',
    'last_name': 'Pal',
    'age': 21,
    'city': 'Lleida',
    },
  
alex93 = {
    'first_name': 'Alexandru',
    'last_name': 'Bejenaru',
    'age': '27',
    'city':'Lleida',
    },
  
paul01 = {
    'first_name':'Paul',
    'last_name':'Pal',
    'age':'19',
    'city':'Lleida',
    },

persons = [bianca99, alex93, paul01]

for person in persons:
  print(f"\n {person}")

# DICTIONARIES IN LISTS

# Make several dictionaries, where each dictionary represents a different pet. In each
# dictionary, include the kind of animal and the owner’s name. Store these dictionaries
# in a list called pets. Next, loop through your list and as you do, print everything
# you know about each pet.

print("\n")

dog = {
  'buldog':'Paul Pal'
}

cat = {
  'british shorthair':'Bianca Pal'
}

turtle = {
  'cumberland':'Alexandru Bejenaru'
}

pets = [dog, cat, turtle]

for pet in pets:
  print(f"\n {pet}")

# LISTS IN DICTIONARIES

# Make a dictionary called favorite_places. Think of three names to use as keys in the
# dictionary, and store one to three favorite places for each person. To make this 
# exercise a bit more interesting, ask some friends to name a few of their favorite 
# places. Loop through the dictionary, and print each person’s name and their favorite
# places.

print("\n")

favorite_places = {
  'Bianca':['Verona', 'London', 'San Sebastian'],
  'Paul':['Venetia', 'Andorra', 'Vielha'],
  'Alexandru':['Tokio', 'New York', 'Germany'],
  }

for name, places in favorite_places.items():
  print(f"\n{name}'s favorite places are:")
  for place in places:
    print(f"\t{place}") 

# LISTS IN DICTIONARIES

# Modify your program from Exercise 6-2 (page 99) so each person can have more than
# one favorite number. Then print each person’s name along with their favorite numbers.

favorite_numbers = {
  'Bianca': [16, 28],
  'Paul':[15, 9],
  'Alexandru': [11,28],
  }

for name, numbers in favorite_numbers.items():
  print(f"\n {name}")
  for number in numbers:
    print(f"\t {number}")

# DICTIONARIES IN DICTIONARIES

# Make a dictionary called cities. Use the names of three cities a keys in your
# dictionary. Create a dictionary of information about each city and include the
# country that the city is in, its approximate population, and one fact about that
# city. The keys for each city’s dictionary should be something like country, population,
# and fact. Print the name of each city and all of the information you have stored 
# about it.

cities = {
  'London' : {
    'country': 'UK',
    'population': '8.982 milion',
    'fact':'Police never caught Jack the Ripper',
    },
  'Bucharest': {
    'country':'Romania',
    'population':'1.83 milion',
    'fact': """The Palace of Parliament is the second largest administrative
             building in the world, right after the Pentagon in the United States.
             It is also the most expensive and the heaviest building in the world.""",
    },
  'Paris': {
    'country': 'France',
    'population': '2.148 milion',
    'fact': 'It is belived that Paris has one stop sign in the entire city.'
    },
  }

for city, properties in cities.items():
  print(f"\n{city}")
  for key, info in properties.items():
    print(f"\t's {key} is {info}")

# We’re now working with examples that are complex enough that they can be extended
# in any number of ways. Use one of the example programs from this chapter, and extend
# it by adding new keys and values, changing the context of the program or improving 
# the formatting of the output.

cities = {
  'London' : {
    'country': ['UK'],
    'demographics': ['8.982 milion', '79.6 men\'s life expectancy','83.8 woman\'s life expectancy'],
    'fact':['Police never caught Jack the Ripper','Feeding pigeons in Trafalgar Square is banned'],
    },
  'Bucharest': {
    'country':['Romania'],
    'demographics':['1.83 milion','73.1 men\'s life expectancy', '79.9 woman\'s life expectancy'],
    'fact': ["""The Palace of Parliament is the second largest administrative
             building in the world, right after the Pentagon in the United States.
             It is also the most expensive and the heaviest building in the world.""","""More than
             10,000 people are bitten by stray-dogs in Bucharest every year."""],
    },
  'Paris': {
    'country': ['France'],
    'demographics': ['2.148 milion','79.8 men\'s life expectancy', '85.7 woman\'s life expectancy'],
    'fact': ['It is belived that Paris has one stop sign in the entire city.',"""The
     main bell of the Notre Dame Cathedral is named Emmanuel and weighs over 13 tonnes."""],
    },
  }

for city, properties in cities.items():
  print(f"\n{city}")
  for info_tag, info in properties.items():
    if len(info) > 1:
      print(f"\t's {info_tag} are {info} ")
    else:
      print(f"\t's {info_tag} is {info}")


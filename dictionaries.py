# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennysilvania', 'California']
# states ['New York', 'NY', 'Pennysilvania', 'PA', 'California', 'CA']

states = {'NY': 'New York', 'PA': 'Pennysilvania', 'CA': 'California'}

print(states['NY'])

people = ["Pal", "Bianca"]

print(type(states))
print(type(people))

print(states.get('FL','Not found'))
print(states.get('NY','Not found'))

print(states.keys())
print(states.values())

# user = ['Bianca', 1.74, 39, 'Blue']
user = {'name': 'Bianca', 'height': 1.74, 'shoe size': 39, 'eye color': 'Blue'}

blog_post = {'title': '11 Sexy Uses for dictionaries', 'body': 'Blah Blah Blah'}

print(user['name'])
print(blog_post['title'])

#dictionaries and lists can be inside of each other

# lists inside of dictionaries
animal_sounds= {
  "cat": ["meow", "purr"],
  "dog": ["woof", "bark"],
  "fox": []
}

# dictionaries inside of lists

Bianca = {'name': 'Bianca', 'height': 1.74, 'shoe size': 39, 'eye color': 'Blue'}
Alex = {'name': 'Alex', 'height': 1.83, 'shoe size': 43, 'eye color': 'Brown'}
Sarah = {'name': 'Sarah', 'height': 1.78, 'shoe size': 40, 'eye color': 'Brown'}

people = [Bianca, Alex, Sarah]

print(people)

# print a key out of people list

for person in people:
    print(person.get('height'))





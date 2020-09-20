# Store information about a person in a dictionary, first name, last name, age and city. Then 
# print call it's key and print the value inside it.
person = {
  'first_name': 'Bianca',
  'last_name': 'Pal',
  'age': 21,
  'city': 'Lleida'
  }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# Use a dictionary to store people's favorite numbers. Think of five names, and store them as 
# keys in your dictionary. Then print each person's name and their favorite number.

favorite_numbers = {
  'Bianca': 16, 
  'Alex': 11,
  'Naomi': 4,
  'Tira': 8,
  'Loe': 7,
  }

print(f"Bianca's favorite number is {favorite_numbers['Bianca']}")
print(f"Alex's favorite number is {favorite_numbers['Alex']}")
print(f"Naomi's favorite number is {favorite_numbers['Naomi']}")
print(f"Tira's favorite number is {favorite_numbers['Tira']}")
print(f"Loe's favorite number is {favorite_numbers['Loe']}")

# Think of five programming words you've learned about in the previous chapters. Use these 
# words as the keys in your glossary, and store their meanings as values.

# Print each word and its meaning as neatly formatted output. You might print the word followed
# by a colon and then it's meaning, or print the word on one line and then print its meaning 
# indented on a second line. Use the newline character (\n) to insert a blank line between each
# word-meaning pair in your output.

programming_words = {
  'for': 'programming structure that repeats a sequence of instructions until a specific condition is met',
  'indentation': 'refers to the spaces at the beginning of a code line that indicate a block of code',
  'comprehension': 'define and create lists based on existing lists',
  'elif': 'the second condition in an if-elif-else conditional structure',
  'tabs': 'Fixed horizontal distance ranged between 4 and 8 spaces long',
  } 

print(f"\nfor:{programming_words['for']}")
print(f"\nindentation:{programming_words['indentation']}")
print(f"\ncomprehension:{programming_words['comprehension']}")
print(f"\nelif:{programming_words['elif']}")
print(f"\ntabs:{programming_words['tabs']}")
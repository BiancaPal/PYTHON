# Write a function called make_shirt() that accepts a size and the text of a message that
# should be printed on the shirt. The function should print a sentence summarizing the size
# of the shirt and the message printed on it. Call the function once using positional 
# arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, text_message):
  print(f"The size of the shirt is {size} and it's message: '{text_message}'.")

make_shirt('M','Love is for free')
make_shirt(size='S',text_message='Do not disturb')

# Modify the make_shirt() function so that shirts are large by default with a message that
# reads I love Python. Make a large shirt and a medium shirt with the default message, 
# and a shirt of any size with a different message.

def make_shirt_default(size='L', text_message='I love Python'):
  print(f"The size of the shirt is {size} and it's messagee: '{text_message}'.'")

make_shirt_default()
make_shirt_default('M')
make_shirt_default('S','Paradise')

# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as Reykjavik is in Iceland. Give the 
# parameter for the country a default value.Call your function for three different cities, 
# at least one of which is not in the default country.

def describe_cities(name, country = 'Iceland'):
  print(f"{name} is in {country}")

describe_cities('Reykjavik')
describe_cities('Selfoss')
describe_cities('London','UK')


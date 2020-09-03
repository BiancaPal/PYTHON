
# functions typically are defined upfront and all the code that runs the functions will be defined later
# return defines what you get back from a fucntion, if you don't call them it will return by defoult "None"
# functions only return 1 thing so anything after the first return it won't work, unless you put a dictionary or list
# you can call functions inside of functions 
# you need to fill in when you run the code, the exact positional arguments you specified above in the function
# you can specify wheh you run the function which positional argument is which"
# variable you define inside of functions are not available outside those functions- scoping



def greet(name):
  return f"Hey {name}!"

def concatenate(word_one, word_two):
  return word_one + word_two

def age_in_dog_years(age):
  result = age * 7
  return result

print(greet('Bianca'))
print(greet('Alex'))

print(concatenate('Bianca', 'Pal'))

print(age_in_dog_years(21))

print(concatenate(word_two='Pal', word_one='Bianca'))

name = "Bianca"

def print_different_name():
  name = "Pal"
  print(name)

print (name)
print_different_name()
print(name)

# Define the function uppercase_and_reverse

def uppercase_and_reverse(str):
  return str.upper()[::-1]

def uppercase(text):
  return text.upper()

def reverse(text):
  return uppercase(text[::-1])

print(uppercase_and_reverse("banana")) 

print(reverse("bananna"))


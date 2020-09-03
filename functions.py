
# functions typically are defined upfront and all the code that runs the functions will be defined later
# return defines what you get back from a fucntion, if you don't call them it will return by defoult "None"
# functions only return 1 thing so anything after the first return it won't work, unless you put a dictionary or list
# you can call functions inside of functions 
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

# PASSING ARGUMENTS

# Positional arguments

# When you call a function, Python must match each argument in the function call with a 
# parameter in the function definition. The simplest way to do this is based on the order
# of the arguments provided. Values matched up this way are called positional arguments.

def describe_pet(animal_type, pet_name):
  """Display information about a pet"""
  print(f"\nI have a {animal_type}.")
  print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','Messi')

# The order of the arguments have to match the exact order of the parameters.

# MULTIPLE FUNCTION CALLS

describe_pet('parrot', 'ciupy')
describe_pet('fish','goldie')

# You can use as many positional arguments as you need in your functions. Python works
# through the arguments you provide when calling the function and matches each one with
# the corresponding parameter in the function's definition.

# Order matters in Positional Arguments: you can get unexpected results if you mix the 
# order of the arguments.

# KEYWORD ARGUMENTS
# A keyword argument is a name-value pair that you pass to a function. You directly 
# associate the name and the value within the argument, so when you pass the argument
# to the function, there's no confusion.

def describe_pet_rewritten(animal_type, pet_name):
  """Display information about your pet"""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.'")

describe_pet_rewritten(animal_type='hamster', pet_name='harry')

# DEFAULT VALUES
# When writting a function, you can define a default value for each parameter. If an 
# argument for a parameter is provided in the function call, Python uses the argument
# value. If not, it uses the parameter's default value. So when you define a default 
# value for a parameter, you can exclude the corresponding argument you'd usually write
# in the function call.

def describe_pet_default(pet_name, animal_type='dog'):
  """Display information about your pet"""
  print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet_default(pet_name='lola')

# Non-default argument follows default argument. This happens because Python still interprets
# this as a positional argument, so if the function is called with just a pet's name, that 
# argument will match up with the first parameter listed in the function's definition.

# To describe an animal other than dog, you could use a function call like this.
describe_pet_default(pet_name='jiji',animal_type='turtle')


# When you use default values, any parameter with a default value needs to be listed after 
# all the parameters that don't have default values. This allows Python to continue interpreting
# positional arguments correctly.


# All the following calls would work for this function.
describe_pet_default('willie')
describe_pet_default(pet_name='willie')

describe_pet_default('harry','hamster')
describe_pet_default(pet_name='harry', animal_type='hamster')
describe_pet_default(animal_type='hamster', pet_name='harry')

# If you don't want to write the keywords, you must define each argument in the same orther
# as the parameters. You can switch the order of the arguments if you include the keywords.

# AVOIDING ARGUMENT ERRORS
# If you try to call a function with no arguments, you'll get an error. Python will tell you
# which are the missing arguments. Also if you provide to many arguments you should get a 
# simmilar traceback.



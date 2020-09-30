# A function doesn't always have to display its output directly. Instead, it can process
# some data and then return a value or set of values. The value the function returns is
# called a return value. The return statement take a value from inside a function and sends
# it back to the line that called the function. Return values allow you to move much of your
# program's grunt work into functions, which can simplify the body of your program.

# Let's look at a function that takes the first and last name and returns a neatly formatted
# full name:

def get_formatted_name(first_name, last_name):
  """Return a full name, neatly formatted"""
  full_name=f"{first_name} {last_name}"
  return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

# To expand the functon with the middle name in between 

def get_formatted_name_all(first_name, middle_name, last_name):
  """Return a full name, neatly formatted"""
  full_name =f"{first_name} {middle_name} {last_name}"
  return full_name.title()

musician = get_formatted_name_all('john', 'lee', 'cooper')
print(musician)

# But middle names aren't always needed, and this function as written would not work if you
# tried to call it with only a fist name and a last name. To make the middle name optional, we
# can give an empty default value and ignore the arguement unless the user provides a value.
# For this we move the middle name to the end of the list of parameters.

def get_formatted_name_default_middle(first_name,last_name,middle_name=''):
  """Return a full name, neatly formatted, with a default middle name!"""

  if middle_name:
    full_name=f"{first_name} {middle_name} {last_name}"
  else:
    full_name=f"{first_name} {last_name}"
  return full_name.title()

programmer = get_formatted_name_default_middle('Bianca','Pal','Maria')
print(programmer)

musician = get_formatted_name_default_middle('John','Cooper','Lee')
print(musician)

# Python interprets non-empty strings as True, if a middle name argument is in the function
# call so if middle_name is provided, the first,middle, and last names are combined to form
# a full name. 

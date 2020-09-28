# FUNCTIONS
# This is a block of code that is designed to do one specific task.
# This is useful if you need to perform that task multiple times throughout your
# program.

# DEFINING FUNCTIONS
def greet_user():
  """Display a simple greeting."""
  print("Hello!")

greet_user()

# def is for letting Python know that you're defining a function, and tells the name of 
# the function, not to forget if applicable, what kind of information the function needs
# to do its job in the parenthesis.

# the indented text between tripple quotes """ """ is a comment called a doctring, which 
# describes what a function does. Docstrings are enclosed in triple quotes, which Python
# looks for when it generates documentation for the functions in your programs.

# If you want to call the function, enter the name of it an parenthesis.

def greet_user(username):
  """Display a simple greeting."""
  print(f"Hello, {username}!")

name = input("Tell me your name: ")
greet_user(name)

# In here we entered username, that allows you to accept any value of username you specify
# Now the function expects you to provide a value for username each time you call it.

# The username is a parameter, a piece of information the function needs to do its job. And 
# the value 'jesse' is an argument, which is a piece of information that's passed from a 
# function call to a function. The argument 'jesse' was assigned to the parameter username.2
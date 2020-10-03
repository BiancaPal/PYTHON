# PASSING AN ARBITRARY NUMBER OF ARGUMENTS
# Sometimes you won't know ahead of time how many arguments a function needs to accept.
# Fortunately, Python allows a function to collect an arbitrary number of arguments from
# the calling statement.

# The function in the following example collects as many arguments as the calling line 
# provides:

def make_pizza(*toppings):
  """Print the list of toppings that have been requested"""
  print(toppings)

make_pizza('pepperoni')
make_pizza('pepperoni','mushrooms','green peppers','extra cheese')

# The asterisk in the parameter name *toppings tells Python to make an empty tuple called
# toppings and pack whatever values it receives into this tuple.

def make_pizza(*toppings):
  """Summarize pizza we are about to make"""
  print("\nMaking pizza with the following toppings: ")
  for topping in toppings:
    print(f"- {topping}")
  
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# MIXING POSITIONAL AND ARBITRARY ARGUMENTS
# If you want a function to accept several different kinds of arguments, the parameter that
# accepts an arbitrary number of arguments must be placed last in the function definition.
# Python as does in the default values, matches positional arguments and keyword arguments first
# an then collects any remaining arguments in the final parameter.

def make_pizza(size,*toppings):
  """Summarize the pizza we are about to make"""
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")
  
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green pepper', 'extra cheese')

# You'll often see the generic parameter name *args, which collect arbitrary positional
# arguments like this:
def make_pizza(size,*args):
  """Summarize the pizza we are about to make"""
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for arg in args:
    print(f"+ {arg}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green pepper', 'extra cheese')

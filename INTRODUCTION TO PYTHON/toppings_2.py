requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
  print(f"Adding {requested_topping}.")

print("\nFinished making your pizza\n")

# An if statement  in the loop could handle the possibility that there isn't 
# any element left

for requested_topping in requested_toppings:
  if requested_topping == 'green peppers':
    print(f"Sorry, we are out of {requested_topping} right now")
  
  else:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

# CHECKING THAT A LIST IS NOT EMPTY

# Soon we'll let users provide the information that's sorted in a list, so we 
# won't be able to assume that a list has any items in it each time a loop is run.
# In this situation, it's useful to check whether a list is empty before running a 
# for loop.

requested_toppings = []

if requested_toppings:
  for requested_topping in requested_toppings:
    print(f"Adding {requested_topping} .")
  print("\nFinished making your pizza")
else:
  print("Are you sure you want a plain pizza")

# When the name of a list is used in an if statement, Python returns True if the 
# list contains at least one item; an empty evaluates to False.

tipe = ''

# TERNARY IN VARIABLE
print("Tiene tipo") if tipe else print("No tiene tipo\n")


# USING MULTIPLE LISTS ( TOPPING REQUESTS FROM AVAILABLE TOPPINGS)

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print(f"Adding {requested_topping}.")
  else:
    print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza")

# We loop through the list of requested toppings, but in there we check to see if each requested topping 
# is actually in the list of available toppings. If it is we add the topping to the pizza else we print 
# that the particular topping which didn't match inside the available toppings is not available.


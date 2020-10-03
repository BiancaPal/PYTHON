# MODIFYING A LIST IN A FUNCTION
# When you pass a list to a function, the function can modify the list. Any changes made to
# the list inside the function's body are permanent, allowing you to work efficiently even
# when you're dealing with large amounts of data.

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
  current_design = unprinted_designs.pop()

  print(f"Printing model: {current_design}")
  completed_models.append(current_design)

print(f"\nThe following models have been printed:")
for completed_model in completed_models:
  print(completed_model)

# As long as there are values in the unprinted_designs list, move the last value's index, 
# to the completed_models list.

print("\n")

def printing_designs(unprinted_designs, printed_designs):

  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")

    printed_designs.append(current_design)


def summarize_prints(printed_designs):
  for printed_design in printed_designs:
    print(printed_design)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
printed_designs = []

printing_designs(unprinted_designs[:], printed_designs)
summarize_prints(printed_designs)

# Every function should have one specific job. If you're writing a function and notice the
# function is doing too many different taks, try to split the code into two functions.
# Remember that you can always call a function from another function, which can be helpful
# when splitting a complex task into a series of steps.

# PREVENTING A FUNCTION FROM MODIFYING A LIST
# If you want to keep track the original list for your records, you can simply address this
# by passing the function a copy of the list, not the original. Any changes the function
# makes to the list will affect only the copy, leaving the original list intact.

# Even though you can preserve the contents of a list by passing a copy of it to your 
# functions, you should pass the original list to functions unless you have specific reason
# to pass a copy. It's more efficient for a function to work with an existing list to avoid
# using the time and memory needed to make a separate copy, especially when you're working
# with large lists.



print(unprinted_designs)
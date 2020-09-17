# TUPLE
# A Tuple is a inmutable list
# It looks like a list except you use parenthesis instead of squared brackets. Once you define a tuple, you can access individual elements by using each item's index, just as you would for a list

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# If you try to change the value of one index you will get 'tuple' object does not support item assignment

# If you want to define a tuple with only just one element you need to defined by the presence of a comma.
my_t = (3,)
print(my_t[0])

# LOOPING THROUGH ALL VALUES OF A TUPLE
for dimension in dimensions:
  print(dimension)

# WRITING OVER A TUPLE
# Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple. So if we wanted to change our dimensions, we could redefine the entire tuple:

print("Original dimensions")
for dimension in dimensions:
  print(dimension)

# Changing the values it's not possible  but yes reassigning a variable is valid.
dimensions = (400, 100)
print("Modified dimensions")
for dimension in dimensions:
  print(dimension)


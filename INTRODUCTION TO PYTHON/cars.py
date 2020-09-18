# Sorting a list permanently with the sort() Method, this will sort the list in alphabetical order, and we can never revert it to the original order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# You can also sort the list in reverse alphabetical order bu passing the argument reverse=True to the sort() method.

cars.sort(reverse=True)
print(cars)

# Sort a list temporarily with te sorted() Function

# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. It displays but doesn't affect the actual order of the list.

cars =  ['bmw', 'audi', 'toyota', 'subaru']
print ("Here is the original list:")
print(cars)

print("\n Here is the sorted list:")
print(sorted(cars))

print("\n Here is the original list again:")
print(cars)

# Permanently reverse the order of a list, wiht reverse() method

print(f"\n{cars}")
cars.reverse()
print(cars)

# You can reverse the changes by applying reverse() again

cars.reverse()
print(cars)

# Finding the length of a list, by using len() function. Python counts the items in a list starting with one, so you shouldn't run into any offby-one-errors when determining the lenght of a list.

print(len(cars))

# IF STATEMENTS
# Python's if statement allows you to examine the current state of a program  and respond appropiately to that state.

for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title())
  
# CONDITIONAL TESTS
# Python uses True and False to decide whether the code in an if statement should be executed. 
# If conditional test evaluates to True, Python executes the code following th if statement.
# If the test evaluates to False, Python ignores the code following the if statement.

# The first line sets the value of car to 'bmw'and the second test checks
# whether the value of a variable is equal to the value of interest:
car = 'bmw'
if car == 'bmw':
  print(True)
else:
  print(False)

# The equality operator returns True if the values on the left and right side of the operator match
# and false if they don't match

# IGNORING CASE WHEN CHECKING FOR EQUALITY
# Two values with different capitalization are not considered equal:

car ='Audi'

if car == 'audi':
  print(True)
else:
  print(False)

# If we convert the value lowecarse before the equality operator it would be true

if car.lower() == 'audi':
  print(True)
else:
  print(False) 



# USING THE RANGE() FUNCTION

# Range() function that makes it easy to generate a series of numbers.d
for value in range (0,5):
  print(value)

print("\n")

# The range() function causes Python to start counting at the first value you give it, and stops when it reaches the second value you provide.
for value in range(0,6):
  print(value)

print("\n")

# OR
for value in range(6):
  print(value) 

print("\n")

# USING RANGE() TO MAKE A LIST OF NUMBERS

# If you want to make a list of numbers, you can convert the results of range() directly to a list using the list() function

numbers = list(range(1,6))
print(numbers)

# THIRD ARGUMENT RANGE()
# If you pass a third argument to range(), Python uses that value as a step size when generating numbers

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Create a set of numbers 

squares  = []
for value in range(1,11):
  square = value ** 2
  squares.append(square)

print(squares)

# OR

squares_alternative = []
for value in range(1,11):
  squares_alternative.append(value**2)

print(squares_alternative)


# SIMPLE STATISTICS WITH A LIST OF NUMBERS

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# LIST COMPREHENSIONS
# A list comprehension allows you to generate this same time list in just one line of code. A list comprehension combines the for loop and the creation of new element into one line, and automatically append each new element.

squares_alternative_2 = [value**2 for value in range(1,11)]
print(squares_alternative_2)

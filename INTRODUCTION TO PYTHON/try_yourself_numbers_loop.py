# Use a foor loop to print the numbers from 1 to 20, inclusive
for number in range (21):
  print(number)

loop_1_to_20 = [value for value in range(1,21)]
print(loop_1_to_20)

# Make a list of numbers from one to one million
numbers = []
for number in range (1_000_001):
  numbers.append(number)

loop_1_to_1000000 = [value for value in range(1, 1_000_000)]
print(loop_1_to_1000000)

# Perform functions min(), max() and sum()
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Use the third argument in the range() function to make a list of odd numbers
for number in range(0,21,2):
  print(number)

loop_odd_numbers = [number for number in range(0,21,2)]
print(loop_odd_numbers)

# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
for number in range(1,30):
  print(3*number)

loop_multiple_of_threes = [number*3 for number in range(1,31)]
print(loop_multiple_of_threes)


# Make a list of the list 10 cubes ( that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
for number in range(1,11):
  print(number**3)

loop_cubes = [number**3 for number in range(1,11)]
print(loop_cubes)


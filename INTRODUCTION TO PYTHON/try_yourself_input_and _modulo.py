# Write a program that asks the user what kind of rental car they would like. Print a 
# message about that car, such as “Let me see if I can find you a Subaru.”

car = input("What kind of rental car would you like?")
print(f"Let me see if I can find you a {car}")

# Write a program that asks the user how many people are in their dinner group. If the
# answer is more than eight, print a message saying they’ll have to wait for a table.
# Otherwise, report that their table is ready.

number = input("How many people are in their dinner group? ")
number = int(number)

if number <= 8:
  print("Your table is ready!")
else:
  print("You'll have to wait for a table")

# Ask the user for a number, and then report whether the number is a multiple of 10 
# or not.

number = input("Write a number: ")
number = int(number)

if number % 10 == 0:
  print(f"The number {number} is multiple of 10")
else:
  print(f"The number {number} is not multiple of 10") 
# SIMPLE IF STATEMENTS

age = 19
if age >= 18:
  print("You're old enough to vote")
  print("Have you registered to vote yet?")

# IF-ELSE STATEMENTS

# The else statement allows you to define an action or set of actions that are executed 
# when the conditional test fails

age = 17
if age >= 18:
  print("You're old enough to vote")
  print("Have you registered to vote yet?")
else:
  print("Sorry, you are too young to vote")
  print("Please register to vote as soon as you turn 18!")

# IF-ELIF-ELSE CHAIN
# Often, you'll need to test more than two possible situations, and to evaluate these
#  you can use Python's if-elif-else syntax. Python executes only one block in an if-elif-else chain
# It runs each conditional test in order until one passes. When a test passes, the code
# following that test is executed and Python skips the rest of the tests.

age = 12

if age < 4:
  cost = 0
elif age < 18:
  cost = 25
else:
  cost = 40

print(f"Your admission cost is ${cost}")

# USING MULTIPLE ELIF BLOCKS
# You can use as many elif blocks in your code as you like.

age = 60

if age < 4:
  cost = 0
elif age < 18:
  cost = 25
elif age < 65:
  cost = 40
else:
  cost = 20

print(f"Your admission cost is ${cost}")

# Python doesn't require an else block at the end of an if-elif chain. 
# Sometimes an elif is clearer , because it catches the specific condition of interest.

age = 65

if age < 4:
  cost = 0
elif age < 18:
  cost = 25
elif age < 65:
  cost = 40
elif age >= 65:
  cost = 20

print(f"Your admission cost is ${cost}")

# The else statement is a catchall statement. It matches any condition that wasn't 
# matched by a specific if or elif test, and that can sometimes include invalid or
# even malicious data.

# If you only want to test for one specific condition you can use if-elif-else
# If you want to check more conditions of interest, because maybe more than one 
# condition is true then you should use a series of simple if statements with no 
# elif or else blocks.

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
  print("Adding mushrooms")

if 'pepperoni' in requested_toppings:
  print("Adding pepperoni")

if 'extra cheese' in requested_toppings:
  print("Adding extra cheese")

print ("\nFinished making your pizza")

# This code wouldn't work properly if we used an if-elif-else block, because the code
# would stop running after only one test passes.

if 'mushrooms' in requested_toppings:
  print("Adding mushrooms")
elif 'pepperoni' in requested_toppings:
  print("Adding pepperoni")
elif 'extra cheese' in requested_toppings:
  print("Adding extra cheese")

print("\nFinished making your pizza")

# In an if-elif-else chain Python doesn't run any tests beyond the first test that 
# passes in an if-elif-else chain. The customer's first topping will be added, but 
# all of their other toppings will be missed:


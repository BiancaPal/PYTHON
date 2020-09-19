alien_color = ['green', 'yellow', 'red']

# Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points. Write one version of this program
# that passes the if test and another that fails. (The version that fails will have 
# no output.)
if 'green' in alien_color:
  print("player_points = 5")

if 'green' not in alien_color:
  print("player_points = 0")


# If the alien’s color is green, print a statement that the player just earned 5 
# points for shooting the alien.


# If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.


# Write one version of this program that runs the if block and another that runs
# the else block.


if 'green' in alien_color:
  print("player_points = 5")
else:
  print("player_points = 10")


# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed for the
# appropriate color alien. 

if 'green' in alien_color:
  print("player_points = 5")
if 'yellow' in alien_color:
  print("player_points = 10")
if 'red' in alien_color:
  print("player_points = 15")

# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 years old but less than 4, print a message that the 
# person is a toddler.
# If the person is at least 4 years old but less than 13, print a message that the
# person is a kid.
# If the person is at least 13 years old but less than 20, print a message that the
# person is a teenager.
# If the person is at least 20 years old but less than 65, print a message that the
# person is an adult.
# If the person is age 65 or older, print a message that the person is an elder.

age = 34

if age < 2:
  print("You're a baby")
elif age >= 2 and age < 4:
  print("You're a toddler")
elif age >= 4 and age < 13:
  print("You're a kid") 
elif age >= 13 and age < 20:
  print("You're a teenager")
elif age >= 20 and age < 65:
  print("You're an adult")
elif age >= 65:
  print("You're an elder")


# Make a list of your three favorite fruits and call it favorite_fruits.
# Write five if statements. Each should check whether a certain kind of fruit is in
# your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!

favorite_fruits = ['fig', 'melon', 'watermelon']

if 'banana' in favorite_fruits:
  print("You really like bananas")

if 'apple' in favorite_fruits:
  print("You really like apples")

if 'fig' in favorite_fruits:
  print("You really like figs")

if 'orange' in favorite_fruits:
  print("You really like oranges")

if 'strawberry' in favorite_fruits:
  print("You really  like strawberries")
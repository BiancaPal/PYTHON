# USING INT() TO ACCEPT NUMERICAL INPUT
# When you use the input() function, Python interprets everything the user enters as 
# a string

#age = input("How old are you? ")

#if age < 18:
#  print("You are unnder eighteen")
#else:
#  print("You are above eighteen")

# When you try to use the input to do a numerical comparison, Python produces an error
# because it can't compare a string to an integer.

# We can solve this issue with the function int() 

height = input("How tall are you, in inches? ")
height = int(height)

if height > 48:
  print("\nYou're tall enough to ride!")
else:
  print("\nYou'll be able to ride when you're a little older.")

# When you use numerical input to do calculations and comparisons, be sure to convert
# the input value to a numerical representation first.

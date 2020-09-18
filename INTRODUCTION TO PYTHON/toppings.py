# CHECKING FOR INEQUALITY
# When you want to determine whether two values are not equal, you can combine an exclamation 
# point(that represents not) with an = (!=)

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
  print("Hold the anchovies!")

# NUMERICAL COMPARISONS
age = 18

if age == 18:
  print("The age is 18!")

answer = 17
if answer != 43:
  print("The answer is not correct!")

# You can include various mathematical comparisons in your conditional statements as well 
# such as less than, less than or equal to, greater than, and greater than or equal to:

age = 19

if age < 21:
  print('The age is less than 21')

if age <= 21:
  print('The age is less or equal than 21')

if age > 21:
  print('The age is greater than 21')

if age >= 21:
  print('The age is greater or equal to 21')

# CHECKING MULTIPLE CONDITIONS
# USING AND TO CHECK MULTIPLE CONDITIONS
# The code inside the if will be execute only if the two conditions are true, if both individual
# Tests pass, the overall conditional expression would be true.

age_0 = 22
age_1 = 18

if age_0 >= 21 and age_1 >=21:
  print(True)
else:
  print(False)

# USING OR TO CHECK MULTIPLE CONDITIONS
# The overall conditional expressions will be true, when either or both of the individual tests 
# pass. An or expression fails only when both individual tests fail.

age_0 = 18

if age_0 >=21 or age_1 >=21:
  print(True)
else:
  print(False)

# CHECKING WHETHER A VALUE IS IN A LIST
requested_topping =['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:
  print("Mushrooms is in list requested topping")
else:
  print('Mushrooms is not in list')


if 'pepperoni' in requested_topping:
  print('Pepperoni is in requested_topping list')
else:
  print('Pepperoni is not in list')


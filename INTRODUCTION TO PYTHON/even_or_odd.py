# THE MODULO OPERATOR
# Devides a number by another number and returns the remainder:

result = (4 % 3)
print(result)

# It only tells you the remainder not how many times one number fits into another.
# When one number is divisible by another number, the remainder is 0, so the modulo
# operator always returns 0. You can use this fact to determine if a number is even 
# or odd:

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
  print(f"The number {number} is even.")
else:
  print(f"The number {number} is odd.")
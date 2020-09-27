# INTRODUCING WHILE LOOPS
# The for loop takes a collection of items and executes a block of code once for each
# item in the collection. In contrast, the while loop runs as long as or while, a certain
# condition is true.


# THE WHILE LOOP IN ACTION
# You can use a while loop to count up through a series of numbers.
current_number = 1
while current_number <= 5:
  print(current_number)
  current_number += 1

# In the first line, we start counting from 1 by assigning current_number the value 1.
# The while loop is then set to keep running as long as the value of current_number is
# less than or equal to 5. The code inside the loop prints the value of current_number
# and then adds 1 to that value with current_number += 1. (The += operator is shorthand
# for current_number = current_number + 1.)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != "quit":
  message = input(prompt)
  
  if message != 'quit':
    print(message)

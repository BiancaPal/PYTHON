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

#while message != "quit":
#  message = input(prompt)
  
#  if message.strip() != 'quit':
#    print(message)

while True:
  parrot = input(prompt)

  if parrot.strip() == 'quit':
    break
  else:
    print(f"I'd love to go to {parrot.title()}")

# USING CONTINUE IN A LOOP

# You can use the continue statement to return to the beginning of the loop to
# return to the beginning of the loop based on the result of a conditional test.

current_number = 0
while current_number <10:
  current_number += 1
  if current_number % 2 == 0:
    continue

  print(current_number)  

# In the following example, the number will increment each time, but if it's even
# it'll not print itself, because it won't arrive to the print statement due to the
# continue statement that tells the code to return to the beginning of the loop.

# The continue statement tells Python to ignore the rest of the loop and return to 
# the beginning.
print("\n")
# AVOIDING INFINITE LOOPS
# Every while loop needs a way to stop running so it won't continue to run forever.
# For example, this counting loop should count from 1 to 5:

x = 1
while x <=5:
  print(x)
  x += 1

# Every programmer accidentally writes an infinite while loop from time to time,
# especially when program's loops have subtle exit conditions. If your program
# gets stuck in infinite loop, press CTRL-C or just close the terminal window 
# displaying your program's output.

# To avoid writing infinit loops, test every while loop and make sure the loop
# stops when you expect it to. If you want your program to end when the user 
# enters a certain input value, run the program and enter that value. If the program
# doesn't end scrutinize the way your program handles the value that should cause
# the loop to exit. Make sure at least one part of the program can make the loop's 
# condition False or cause it to reach a break statement.
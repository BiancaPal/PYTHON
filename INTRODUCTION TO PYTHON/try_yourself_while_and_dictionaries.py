# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. Loop through the list of sandwich
# orders and print a message for each order, such as I made your tuna sandwich. As each
# sandwich is made, move it to the list of finished sandwiches. After all the sandwiches
# have been made, print a message listing each sandwich that was made.

sandwich_orders = ['York', 'Jamón y queso', 'Tortilla', 'Fuet', 'Longaniza']
finished_sandwiches=[]

while sandwich_orders:
  
  finished_order=sandwich_orders.pop()

  print(f"I made you a {finished_order} sandwich!")

  finished_sandwiches.append(finished_order)

for finished_sandwich in finished_sandwiches:
  print(finished_sandwich)

# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' 
# appears in the list at least three times. Add code near the beginning of your program
# to print a message saying the deli has run out of pastrami, and then use a while loop
# to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami 
# sandwiches end up in finished_sandwiches.

print("\n")

sandwich_orders = ['York','pastrami', 'Jamón y queso', 'pastrami', 'pastrami', 'Tortilla', 'Fuet', 'Longaniza']

print("Deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')

for sandwich_order in sandwich_orders:
  print(sandwich_order)

# Write a program that polls users about their dream vacation. Write a prompt similar to If
# you could visit one place in the world, where would you go? Include a block of code that 
# prints the results of the poll.

prompt = "If you could visit one place in the world, where would you go?"
status = True

while status:
  place = input(prompt)
  print(f"Wow,{place}, what an interesting place!")
  status = False


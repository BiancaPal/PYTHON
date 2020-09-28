toppings = []
# Write a loop that prompts the user to enter a series of pizza toppings until 
# they enter a 'quit' value. As they enter each topping, print a message saying
# you’ll add that topping to their pizza.
prompt="Enter some pizza toppings: "
status = True
while status:
  pizza_toppings= input(prompt)
  if pizza_toppings.strip() == 'quit':
    break
  else:
    print(f"I'll add to your pizza {pizza_toppings.title()}")
    toppings.append(pizza_toppings)

print(toppings)
# A movie theater charges different ticket prices depending on a person’s age.
# If a person is under the age of 3, the ticket is free; if they are between 3
# and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, and then tell them the cost of 
# their movie ticket.

prompt="Enter your age: "
status = True
quit=1
while status and quit < 2:
  age = input(prompt)
  age_int=int(age)

  if age_int <3:
    print("The ticket is free")
  elif age_int >=3 and age_int <=12:
    print("Your ticket is 10$")
  elif age_int >=12:
    print("Your ticket is 15$")
    quit +=1
  


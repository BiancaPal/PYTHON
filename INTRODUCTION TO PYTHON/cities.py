# USING BREAK TO EXIT A WHILE LOOP
# To exit a while loop immediately without running any remaining code in the loop,
# regardless of the results of any conditional tests, use the break statement.
# The break statement directs the flow of your program; you can use it to control 
# which lines of code are executed and which aren't, so the program only executes 
# code that you want it to, when you want it to.



prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you're finished.) "

while True:
  city = input(prompt)

  if city == 'quit':
    break
  else:
    print(f"I'd love to go to {city.title()}!")

# A loop that starts with while True will run forever unless it reaches a break
# statement. 
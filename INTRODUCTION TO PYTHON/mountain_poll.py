responses = {}

# Set a flag indicating the poll is active.
polling_status = True

while polling_status:
  name = input("\nWhat is your name? ")
  response = input("Which mountain would you like to climb someday? ")
  #Store the output into the dictionary, with the key as the name and the value as the response
  responses[name] = response

  repeat = input("Would you like another person to respond? (Yes/No) ")
  repeat = repeat.lower()
  if repeat.strip() =='no':
    polling_status=False

print("\n--- Poll results ---")
for name, response in responses.items():
  print(f"{name} would you like to climb {response}")

# The program first defines an empty dictionary, and then defines the status to True. While the
# condition is true, the name and the response will be stored in a dictionary as a key and value.
# We will put the lower method in the repeat question. And break the while statement by modifying
# the condition to False.
answer = input ("Do you want to hear a joke?")

affirmative_responses = ["yes", "Yes", "Y" , "y"]
negative_responses = ["No", "no", "N", "n"]

if answer in affirmative_responses:
  print("I'm against picketing, but I don't know how to show it.")

elif answer in negative_responses:
  print("Fine")
else:
  print("I don't understand")
# In the while loop, we had the program perform certain tasks while a given condition was true.
# But what about more complicated programs in which many different events could cause the program
# to stop running.

# If many possible events might occur to stop the program, trying to test all these conditions in
# on while statement becomes complicated and difficult.

# For a program that should run only as long as many conditions are true, you can define one variable
# that determines whether or not the entire program is active. This variable, called flag, acts as a
# signal to the program.

prompt = "\nTell me something, and I will repeat it back to you: "
prompt +="\nEnter 'quit' to end the program."

active = True
while active:
  message = input(prompt)

  if message == 'quit':
    active = False
  else:
    print(message)

# We set the variable active to True, so the program starts in an active state.


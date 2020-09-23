# USER INPUT AND WHILE LOOPS

# Most programs are written to solve an end user's problem. To do so, you usually need
# to get some information from the user. For a simple example, let's say someone wants
# to find out whether their are old enough to vote.

# To do this you'll need to use the input() function.

# You'll also learn how to keep programs running as long as users want them to, so 
# they can enter as much information as they need to; then, your program can work with
# that information. You'll use Python's while loop to keep programs running as long as 
# certain conditions remain true.

# INPUT ()
# The input function takes one argument: the prompt, or instructions, that we want to 
# display to the user so they know what to do. In this example, when Python runs the 
# first line, the user sees the prompt Tell me something, and I will repeat it back 
# to you:. The program waits while the user enters their response and continues after
# the user presses ENTER. The response is assigned to the variable message, and print it.


message = input("Tell me something, and I will repeat it back to you: ")
print(message)


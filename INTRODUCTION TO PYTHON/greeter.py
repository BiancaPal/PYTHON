# It's important to write clear, easy to follow prompt that tells the user exactly what
# kind of information you're looking for.

name = input("Please write your name: ")
print(f"\nHello, {name}!")

# It's also important to write a space at the end of your prompts (after the colon in
# the preceeding example) to separate the prompt from the user's response and to make
# it clear to your user where to enter their text.

# Sometimes you'll want to write a prompt that's longer than one line. You can assign
# your prompt to a variable and pass that variable to the input() function. This allows
# you to build your prompt over several lines, then write a clean input() statement.

prompt = "If you tell us who you are, we can personalize the messages you see."
# The operator += takes the string that was assigned to prompt and adds the new string 
# onto the end.
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"Hello, {name}")

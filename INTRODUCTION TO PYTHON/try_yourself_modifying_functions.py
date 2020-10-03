
# Make a list containing a series of short text messages. Pass the list to a function called
# show_messages(), which prints each text message.

def show_messages(messages):
  for message in messages:
    print(f"{message}")


messages = ['Hello,how are you?','What\'s upp', 'How ya\' doin\' folks?']
show_messages(messages)

# Start with a copy of your program about modifying lists. Write a function called send_messages()
# that prints each text message and moves each message to a new list called sent_messages
# as it's printed. After calling the function, print both of your list to make sure the 
# messages were moved correctly.

def send_messages(messages,sent_messages):
  while messages:
    current_message = messages.pop()
    print(f"The message '{current_message}' has been sent. ")
    sent_messages.append(current_message)

# Call the function send_messages() with a copy of the list og messages. After calling the
# function, print both of your lists to show that the original list has retained its messages.

messages = ['Hello,how are you?','What\'s upp', 'How ya\' doin\' folks?']
sent_messages = []

send_messages(messages[:],sent_messages)

print(messages)
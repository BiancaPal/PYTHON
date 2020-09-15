# A list is a collection of items in a particular order. 
# In Python square brackets [] indicate a list, and individual elements in the list are separated by commas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Python returns its representations of the list, including the square brackets:
# ['trek', 'cannondale', 'redline', 'specialized']

# Because this isn't the output you want your users to see, we will access the elements list by telling Python the position, or index, of the item desired.
# The following way will display a clean, neatly formatted output
print(bicycles[0])
print(bicycles[0].title())

# Python considers the first item in a list to be at position 0, not position 1. Using the counting system, you can get any element you want from a list by substracting one from the postion in the list.
print(bicycles[1])
print(bicycles[3])

# Python has a special syntax for accessing the last element in a list. By asking for the item at index -1.
print(bicycles[-1])
# This convention extends to other negative index values as well. The index -2 returns the second item from the end of the list, and so forth.
print(bicycles[-2])

# You can use f-strings to create a message based on a value from a list.
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

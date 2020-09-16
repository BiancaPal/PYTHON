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

# For modifying elements in a list, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0]= 'ducati'
print(motorcycles)

# To append elements to the end of a list use the method .append('insert the element')

motorcycles.append('honda')
print(motorcycles)

cars = []

cars.append('citroen')
cars.append('audi') 
cars.append('bentley')
cars.append('ferrari') 
cars.append('lamborghini')

print(cars)

# To insert Elements into a list, we call the insert() method, in the parentheses you'll need to specify the position, and the element.
# The insert method opens a space at the position you specified and stores the value in that location.
cars.insert(5,'jaguar')
print(cars)

# To remove an item or a set of items from a list.
del cars[0]
print(cars)

# To remove the last item of a list, but it lets you work with that after removing it.
print(cars)

popped_cars = cars.pop()
print(cars)
print(popped_cars)
print(f"The last car I owned was a {popped_cars}")

# You can pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses.

first_owned = cars.pop(0)
print(f"The first car I owned was a {first_owned}")

# Sometimes you don't know the exact index of the value in the list, then you can use remove() method

cars.remove('ferrari')
print(cars)

# You can also remove() method to work with a value that's being removed from a list.

too_expensive= 'lamborghini'
cars.remove(too_expensive)
print(cars)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# The remove() method deletes only the first occurrence of the value you specify. If there's a possibility the value appears more than oncein the list, you'll need to usr a loop to make sure all the occurrencies of the value are removed.


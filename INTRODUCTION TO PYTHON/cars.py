# Sorting a list permanently with the sort() Method, this will sort the list in alphabetical order, and we can never revert it to the original order

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# You can also sort the list in reverse alphabetical order bu passing the argument reverse=True to the sort() method.

cars.sort(reverse=True)
print(cars)

# Sort a list temporarily with te sorted() Function

# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. It displays but doesn't affect the actual order of the list.

cars =  ['bmw', 'audi', 'toyota', 'subaru']
print ("Here is the original list:")
print(cars)

print("\n Here is the sorted list:")
print(sorted(cars))

print("\n Here is the original list again:")
print(cars)

# Permanently reverse the order of a list, wiht reverse() method

print(f"\n{cars}")
cars.reverse()
print(cars)

# You can reverse the changes by applying reverse() again

# Finding the length of a list, by using len() function. Python counts the items in a list starting with one, so you shouldn't run into any offby-one-errors when determining the lenght of a list.

print(len(cars))

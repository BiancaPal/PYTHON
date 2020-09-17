# COPYING A LIST
# To copy a list you can make a slice that includes the entire original list by ommitting the first index and the second index ([:]). This tells Python to make a slice that starts at the first item and ends with the last item.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\n My friend's favorite foods are")
print(friend_foods)

# This would be proof that we actually have separate different lists

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

# This won't work, because the following syntax will tell Python to associate the new variable friend_foods with the list that is already associated woth my_foods, so now both variables point to the same list.

friend_foods=my_foods

my_foods.append('cannoli')
print(my_foods)

friend_foods.append('ice cream')
print(friend_foods)


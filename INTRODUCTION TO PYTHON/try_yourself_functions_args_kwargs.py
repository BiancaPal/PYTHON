# Write a function that accepts a list of items a person wants on a sandwich. The function
# should have one parameter that collects as many items as the function call, provides, and
# it should print a summary of the sandwich that's being ordered. Call the function three 
# times, using a different number of arguments each time.

def make_sandwich(*ingredients):
  for ingredient in ingredients:
    print(f"We're adding {ingredient}")
  print("Your sandwhich is ready for pickup")

make_sandwich('cheese','olives','fuet')
make_sandwich('tortilla')
make_sandwich('cherry tomatoe','oil')

# Build a profile of yourself by calling build_profile(), using your first and last names and
# three other key-value pairs that describe you.

def build_profile(first, last, **kwargs):
  kwargs['first_name'] = first
  kwargs['last_name'] = last
  return kwargs


user_1 = build_profile('Bianca','Pal',age=21,country='Spain')
print(user_1)

# Write a function that stores information about a car in a dictionary. The function should 
# always receive a manufacturer and a model name. It should then accept an arbitrary number
# of keyword arguments. Call the function with the required information and two other name-value
# pairs, such as a color or an optional feature. Your function should work for a call like 
# this one.

def make_car(manufacturer,model_name,**kwargs):
  kwargs['manufacturer'] = manufacturer
  kwargs['model_name'] = model_name
  return kwargs


model_1 = make_car('subaru','outback',color='blue',tow_package=True)
print(model_1)
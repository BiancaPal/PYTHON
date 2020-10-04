# USING ARBITRARY KEYWORD ARGUMENTS
# Sometimes you'll want to accept an arbitrary number of arguments, but you won't know ahead
# of time what kind of information will be passed to the function. In the following function
# you'll know that the last and first name will be included but the rest are arbitrary number
# of positional keyword arguments.


def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user"""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('albert', 'einstein',
                            location = 'princeton',
                            field = 'physics')

print(user_profile)

# The ** before the parameter **user _info cause Python to create an empty dictionary called
# user_info and pack whatever name-value pairs it receives into this dictionary.

# You'll often see the parameter name **kwargs used to collect non-specific keyword arguments
def build_profile_2(first, last, **kwargs):
  """Build a dictionary containing everything we know about a user"""
  kwargs['first_name'] = first
  kwargs['last_name'] = last
  return kwargs

user_profile_2 = build_profile_2('albert', 'einstein',
                                 location = 'princeton',
                                 field = 'physics',
                                 years = 67)

print(user_profile_2)
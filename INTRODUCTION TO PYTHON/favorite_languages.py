favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
  }

# It's good practice to include a comma after the last key-value pair as well, so you're ready to 
# add a new key-value pair on the next line.

language = favorite_languages['sarah'].title()

print(f"Sarah's favorite language is {language}.")

# USING GET TO ACCESS VALUES
# Using keys in square brackets to retrieve the value you're interested in from a dictionary might
# cause one potential problem: if the key you asked for doesn't exist, you'll get an error.

# The get() method requires a key as a first argument. As a second optional argument, you can pass
# the value to be returned if the key doesn't exist.

point_value = favorite_languages.get('python', 'No point value assigned')
print(point_value)

# If the key 'python' exists in the dictionary, you'll get the corresponding value. If it doesn't
# you get the default value. In this case, points doesn't exist, and we get a clean message 
# instead of an error:

# If there's a chance the key you're asking for might not exist, consider using the get() method 
# instead of the square bracket notation.

# If you leave the second argument of the get() method empty, Python will return None.(absence of
# value)




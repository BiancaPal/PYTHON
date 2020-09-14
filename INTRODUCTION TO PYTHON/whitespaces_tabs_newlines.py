print("Python")
print("\tPython")
print("\n\tPython\n\tC\n\tJavascript")
print("Python")
print("Python")

# Strippint whitespace
# To a program, 'python ' and 'python' are two different strings. Python detects the extra space in 'python ' and considers it significant unless you tell it otherwise.
# That's why rstrip() can look for extra whitespace on the right and left sides of a string.

favorite_language = ' python '

# to strip the whitespace from the right side
favorite_language.rstrip()
# to strip the whitespace from the left side
favorite_language.lstrip()
# to strip the whitespace from both left and right sides 
favorite_language.strip()


# This stripping functions are used most often to clean up user input before it's stored in a program



# STORING YOUR FUNCTIONS IN MODULES

# One advantatge of functions is the way they separate blocks of code from your main program.
# By using descriptive names for your functions, your main program will be much easier to 
# follow. You can go a step further by storing your functions in a separate file called
# module and then importing that module into your main program. An import statement tells 
# Python to make the code in a module available in the currently running programming file.

# Storing your functions in a separate file allows you to hide the details of your program's
# code and focus on its higher-level logic. It also allows you to reuse functions in many 
# different programs. When you store your functions in separate files, you can share those
# files wiht other programmers without having to share your entire program. Knowing kow to 
# import functions also allows you to use libraries of functions that other programmers have
# written. 

# There are several ways to import a module, and I'll show you each of these briefly.

# You have create a module, that is to remove everything apart from the function.
# Now you'll have to make another file that will be using the function in the module.

# The file imports the module we just created and then makes two calls to make_pizza():

import pizza_module

pizza_module.make_pizza(16,'pepperoni')
pizza_module.make_pizza(12,'mushrooms','green peppers','extra cheese')

# When Python reads this file, the line import pizza_module tells Python to open file pizza_module.py
# and copy all the functions from it into this program. You don't actually see code being
# copied between files because Python copies the code behind the scenes just before the program
# runs. All you need to know is that any function defined in pizza_module.py will now be 
# available in making_pizzas.py.

# To call a function from an imported module, enter the name of the module you imported, pizza
# followed by the name of the function. Separated by a dot. This code produces the same output
# as the original program that didn't import a module:

# module_name.function_name() <= THAT IS THE STRUCTURE TO USE THE FUNCTION

# IMPORTING SPECIFIC  FUNCTIONS
# You can also import specific function from a module. Here's the general syntax for this approach:

from pizza_module import make_pizza

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

# Also you can import as many functions as you want from a module by separating each function's
# name with a coma:
# from module_name import function_0, function_1, function_2

# With this syntax you don't need to use the dot notation when you call a function. Because
# we've explicitly imported the function make_pizza() in the import statement, we can call it
# by name when we use the function.

# USING AS TO GIVE A FUNCTION AN ALIAS
# If the name of a function you're importing might conflict with an existing name in your 
# program or if the function name is long, you can use a short, unique alias- an alternative
# name simmilar to a nickname for the function. You'll give the function this special nickname
# when you import the function.

# Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp. The
# as keyword renames a function using the alias you provide:

from pizza_module import make_pizza as mp

mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheeese')

# The general syntax for providing an alias is:
# from module_name import function_name as fn

# USING AS TO GIVE A MODULE AN ALIAS
# You can also provide an alias for a module name. Giving a module a short alias, like p for
# pizza, allows you to call the module's functions more quickly. Calling p.make_pizza() is
# more concise than calling pizza.make_pizza()

import pizza_module as p 

p.make_pizza(16,'pepperoni')ç
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

# Calling the functions by writing p.make_pizza() is not only more concise than writing pizaa.make_pizza()
# but also redirects your attention from the module name and allows you to focus on the descriptive
# names of its functions. These function names, which clearly tell you what each function does,
# are more important to the readability of your code than using the full module name.

# The general syntax for this approach is:
# import module_name as mn

# IMPORTING ALL FUNCTIONS IN A MODULE
# You can tell Python to import every function in a module by using the asterisk(*) operator

from pizza_module import *

make_pizza(16, 'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
# The astetisk * tells Python to copy every function from the module pizza into its program file.
# Because every function is imported you can call any function wihout the name or the alias of
# the module. However it's best not to use this approach when you're working with larger modules
# that you didn't write: if the module has a function name that matches an existing name in your
# project, you can get some unexpected results. Python may see several functions or variables
# with the same name, and instead of importing all the functions separately,it will overwrite
# the functions.

# The best approach is to import the function or functions you want, or import the entire module
# and use the dot notation. This leads to clear code that's easy to read and understand. I
# include this section so you'll recognize import statements like the following when you see
# them in other people's code:




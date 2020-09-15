# INTEGERS
# You can add (+), subtrac(-), multiply(*), and devide (/) integers in Python
# To represent exponents Python uses two multiplication symbols
# Python supports the order of operations too, so you can use multiple operations in one expression. You can also use parentheses to modify the order of operations so Python can evaluate your expression in the order you specify

# FLOATS
# Python calls any number with a decimal point a float. Python tries to find a way to represent the result as precisely as possible, which is sometimes difficult fiven how computers have to represent numbers internally.

# FLOATS AND INTEGERS
# When you devide any two numbers, even if they are integers that result in a whole number, you'll always get a float
# If you mix an integer and float in any other operation, you'll get a float as well
# Python defaults to a float in any operation that uses a float, even if the output is a whole number.

# UNDERSCORES IN NUMBERS
# When you are writting long numbers, you can group digits using underscores to make larg numbers more readable like 14_000_000_000
# Python ignores the underscores when storing these kinds of values. Even if you don't group the digits in threes the values will still be unaffected. To Python's version 3.6 and later, 1000 is the same as 1_000 and 10_00

# MULTIPLE ASSIGNMENT
# You can assign values to more than one variable using just a single line. In this format x, y, z = 0, 0, 0 as long as the number of values matches the numbers of variables, Python will match them correctly.

# CONSTANTS 
# A constant is like a variable whose value stays the same throughout the life of a program. Python doesn't have built-in constant types, but Python programmers use all capital letters to indicate a variable should  be treated as a constant and never be changed.
# MAX_CONNECTIONS = 5000

#>>> 2+3
#5
#>>> 3-2
#1
#>>> 2*3
#6
#>>> 3/2
#1.5
#>>> 3 ** 3
#27
#>>> 3 ** 2
#9
#>>> 10 **6
#1000000
#>>> 2 + 3*4
#14
#>>> (2+3) *4
#20
#>>> 0.2+0.1
#0.30000000000000004
#>>> 0.1+0.1
#0.2
#>>> 3*0.1
#0.30000000000000004
#>>> 4/5
#0.8
#>>> 4/8
#0.5
#>>> 8/4
#2.0
#>>> universe_age=14_000_000_000
#>>> print(universe_age)
#14000000000
#>>> x, y, z = 0,0,0
#>>> print(x)
#>>> MAX_CONNECTIONS = 5000
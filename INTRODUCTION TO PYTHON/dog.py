# CLASSES

# Object-oriented programming is one of the most effective approaches to writting software.
# In object-oriented programming you write classes that represent real-world things and situations
# and you create objects based on these classes. When you write a class, you define the general
# behavior that a whole category of objects can have.

# When you create individual objects from the class, each object is automatically equipped
# with the general behaviour; you can then give each object whatever unique traits you
# desire. You'll be amazed how well real-world situations can be modeled with object-oriented
# programming.

# Making an object from a class is called instantiation, and you work with instances of a class.
# In this chapter you'll write classes and create instances of those classes. You'll specify
# the kind of information that can be stored in instances, and you'll define actions that can
# be taken with these instances. You'll write classes that extend the functionality of existing
# classes, so similar can be share code efficiently. You'll store your classes in modules and
# import classes written by other programmers into your own program files.

# Understanding classes, will help you really know your code, not just what's happening line by
# line, but also the bigger concepts behind it. Knowing the logic behind classes will train you
# to think logically so you can write  programs that effectively address almost any problem
# you encounter.

# CREATNG AND USING A CLASS
# The following class will tell Python how to makean object representing a dog. After our class
# is written, we'll use it to make individual instances, each of which represents one specific
# dog.

# CREATING A DOG CLASS
# Each instance created from the Dog class will store a name and and an age, and we'll give
# each dog the ability to sit() and roll_over():

class Dog:
  """ A simple attempt to model a dog"""

  def __init__(self, name, age):
    """Initialize name and age attributes"""
    self.name = name
    self.age = age
  
  def sit(self):
    """Simulate a dog sitting in response to a command"""
    print(f"{self.name} is now sitting.")
  
  def roll_over(self):
    """Simulate a dog rolling over in response to a command"""
    print(f"{self.name} roll over!")

# By convention, capitalized names refer to classes in Python. There are no parenthesis in 
# the class definition because we're creating this class from scratch. Then we write a
# docstring describing what this class does.


# The __init__() Method
# A function that's part of a class is a method. Everything you learned about functions applies
# to methods aswell; the only practical difference for now is the way we'll call methods.
# The ___init__ method is a special method that Python runs automatically whenever we create
# a new instance based on the Dog class. This method had two leading underscores and two trailing
# underscores, a convention that helps prevent Python's default method names from conflicting
# with your method names. Make sure to use two underscores on each side of __init__(). If you
# use just one on each side, the method won't be called automatically when you use your class,
# which can result in errors that are difficult to identify.

# We define the __init__() method to have three parameters: self, name, and age. The self parameter
# is required in the method definition, and it must come first before the other parameters. It
# must be included in the definition because when Python calls this method later (to create an
# instance of Dog), the method call will automatically pass the self argument. Every method
# call associated with an instance automatically pass the self argument, which is a reference
# to the instance itself; it gives the individual instance access to the attributes and methods
# in the class. When we make an instance of Dog, Python will call the __init__() method from
# the Dog class. We'll pass Dog() a name and an age as arguments; self is passed automatically,
# so we don't need to pass it. Whenever we want to make an instance from the Dog class, we'll
# provide values for only the last two parameters, name and age.

# The two variables defined have the same prefix self. Any variable prefixed with self is 
# available to every method in the class, and we'll also be able to access these variables
# through any instance created from the class.

# The line self.name = name takes the value associated with the parameter name and assigns
# it to the variable name, which is then attached to the instance being created. The same 
# process happens with self.age = age. Variables that are accessible through instances like 
# this are called attributes.

# The dog class has two other methods defined: sit() and roll_over().
# Because these methods don't need additional information to run, we just define them to have
# one parameter, self. The instances we create later will have access to these methods.
# In other words, they'll be able to sit and roll over. 


# MAKING AN INSTANCE FROM A CLASS

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
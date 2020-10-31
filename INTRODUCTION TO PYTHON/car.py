# WORKING WITH CLASSES AND INSTANCES

# You can use classes to represent many real-world situations. Once you write a class,
# you'll spend most of your time working with instances created from that class. One of
# the first tasks you'll want to do is modify the attributes associated with a particular
# instance directly or write methods that update attributes in specific ways.

# THE CAR CLASS

class Car:
  """A simple attempt to represent a car!"""

  def __init__(self, manufacturer, model, year):
    """Initialize attributes to describe a car"""
    self.manufacturer = manufacturer
    self.model = model
    self.year = year
  
  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name =f"{self.year} {self.manufacturer} {self.model}"
    return long_name.title()
  

my_new_car = Car("Audi",'a4',2019)
print(my_new_car.get_descriptive_name())

# SETTING A DEFAULT VALUE FOR AN ATTRIBUTE
# When an instance is created, attributes can be defined without being passed in as
# parameters. These attributes can be defined in the __init__() method, where they are
# assigned a default value.

# Let's add an attribute called odometer_reading that always statrs with a value of 0.
# We'll also add a method read_odometer() that helps us read each car's odometer:

class Car:
  
  def __init__(self, make, model, year):
    """Initialize attributes to describe a car"""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  
  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name =f"{self.year} {self.make} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
    """Print a statement showing the car's mileage"""
    print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi','a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# MODIFYING ATTRIBUTE VALUES
# You can change an attribute's value in three ways: you can change the value directly 
# through an instance, set the value through a method, or increment the value (add a 
# certain amount to it) through a method. Let's look at each of these approaches.

# MODIFYING AN ATTRIBUTE'S VALUE DIRECTLY
# The simplest way to modify the value of an attribute is to access the attribute directly 
# through an instance. Here we set the odometer reading to 23 directly.

my_second_new_car = Car('audi','a7', 2019)
print(my_second_new_car.get_descriptive_name())

my_second_new_car.odometer_reading = 23
my_second_new_car.read_odometer()

# MODIFYING AN ATTRIBUTE'S VALUE THROUGH A METHOD

class Car:
  def __init__(self, make, model, year):
    """Initialize attributes to describe a car"""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  
  def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name =f"{self.year} {self.make} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
    """Print a statement showing the car's mileage"""
    print(f"This car has {self.odometer_reading} miles on it.")
  
  def update_odometer(self, mileage):
    """Set the odometer reading to the given value"""
    self.odometer_reading = mileage
  
my_third_new_car = Car('audi','a7', 2019)
print(my_third_new_car.get_descriptive_name())

my_third_new_car.update_odometer(23)
my_third_new_car.read_odometer()

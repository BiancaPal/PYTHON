# Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open. 
class Restaurant:
  """Attempt to model a restaurant"""

  def __init__(self, restaurant_name, cuisine_type):
    """Initialize restaurant name and cuisine type"""
    self.name = restaurant_name
    self.type = cuisine_type
  
  def describe_restaurant(self):
    """Describe the restaurant"""
    print(f"The restaurant's name is {self.name} and the type of its cusine is {self.type}.")

  def open_restaurant(self):
    """Simullate the opening of a restaurant"""
    print(f"{self.name} is now open!")

# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.
first_restaurant = Restaurant('The NewOrleans','Cajún')

print(f"The new restaurant's name is {first_restaurant.name}")
print(f"The new restaurant's type of cuisine is {first_restaurant.type}")

first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()

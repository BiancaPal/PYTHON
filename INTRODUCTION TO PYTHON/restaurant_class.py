class Restaurant:
  """A simple attempt to model a Restaurant"""

  def __init__(self, restaurant_name, cuisine_type):
    """Initialize name and type attributes"""
    self.name = restaurant_name
    self.type = cuisine_type
  
  def describe_restaurant(self):
    """Describe a restaurant """
    print(f"The restaurant's name is {self.name} and it's cuisine type is {self.type}")
  
  def open_restaurant(self):
    """Simulate the opening of a restaurant"""
    print(f"The restaurant {self.name} is opening!")

my_restaurant = Restaurant('bbg','burguer')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_second_restaurant = Restaurant('Lo Brull','Mediterranian')

my_second_restaurant.describe_restaurant()
my_second_restaurant.open_restaurant()

my_third_restaurant = Restaurant('El paso del diablo','Mexican')

my_third_restaurant.describe_restaurant()
my_third_restaurant.open_restaurant()


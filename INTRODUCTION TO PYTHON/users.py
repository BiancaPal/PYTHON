class User:
  """An attempt to model a user"""

  def __init__(self, first_name, last_name,*attributes):
    """Initialize the attributes"""
    self.first_name = first_name
    self.last_name = last_name
    self.attribute = attributes
  
  def describe_user(self):
    print(f"The user's first_name is {self.first_name} and it's last  is {self.last_name}")
  
  def greet_user(self):
    print(f"Hello, welcome to the community {self.first_name} {self.last_name}!")


user_1 = User("Bianca", "Pal")

user_1.describe_user()
user_1.greet_user()

user_2 = User("Alexandru", "Bejenaru")

user_2.describe_user()
user_2.greet_user()

user_3 = User("Dario", "Bejenaru")

user_3.describe_user()
user_3.greet_user()

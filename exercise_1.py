import random

meals = ["Mango Smoothie",
         "Egg sandwich",
         "Burrito",
         "Crispy egg toast",
          "Ham wich", 
          "Spinach and prosciutto frittata muffin",
          "Banana split oatmeal",
          "Banana bread",
          "Greek yogurt with oatmeal and fruits",
          "Waffle"]



random_meal = random.choice(meals)


print(f"How about you prepare yourself a {random_meal} ?")

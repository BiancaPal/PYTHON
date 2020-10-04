def make_pizza(size,*args):
  """Summarize the pizza we are about to make"""
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for arg in args:
    print(f"+ {arg}")


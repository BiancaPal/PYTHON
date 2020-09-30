def get_formatted_name(first_name, last_name):
  """Return a full name, neatly formatted."""
  full_name = f"{first_name} {last_name}"
  return full_name.title()

while True:
  print("\nPlease tell me your name:")
  print("Enter 'q' anytime to quit")
  f_name = input("First name: ")
  if f_name == 'q':
    break
  l_name = input("Last name: ")
  if l_name == 'q':
    break


  formatted_name = get_formatted_name(f_name, l_name)
  print(f"\nHello, {formatted_name}")

# The program keeps greeting people until someone puts 'q' in any of the inputs.

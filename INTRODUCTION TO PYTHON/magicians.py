# LOOP THROUGH AN ENTIRE LIST

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(f"{magician.title()}, that was a great trick!")
  print(f"I can't wait to see your next trick, {magician.title()}.\n")

# It's helpful you choose a variable that is associated with each value in the list.
# Naming conventions like, for cat in cats: or for dog in dogs:

print("Thank you, everyone. That was a great magic show!")

# INDENTATIONN are considered the four whitespaces, that forces you to write neatly formmated code with a clear visual structure.

# - 1.ERROR: forgetting to indent that is

# for magician in magicians:
# print(magician)

# - 2.ERROR: forgetting to indent additional lines

# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
# print(f"I can't wait to see your next trick, {magician.title()}.\n")

# - 3.ERROR: indenting unnecessarily
# message = "Hello Python world"
#    print(message)

# - 4.ERROR: indenting unnecessarily after the loop
# for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")
#    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#    print("Thank you everyone, that was a great magic show!")

# - 5.ERROR: forgetting the colon ":"
# for magician in magicians
#    print(magician)



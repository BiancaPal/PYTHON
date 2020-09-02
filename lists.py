the_count = [1, 2, 3, 4, 5]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Anthony Weiner", 1/2, ["Oh no"]]

#this for loop goes through a list

for number in the_count:
  print("this is count", number)

#same as the above

for stock in stocks:
  print("Stock ticker:", stock)

for i in random_things:
  print("Here's a random thing:", i)

#we can also build lists, first let's start with an epmty one

people = []

people.append("Mattan")
people.append("Sarah")
people.append("Chris")

#now we can print them out too
print(people)

#and remove some
people.remove("Sarah")
print(people)

for person in people:
  print("Person is:", person)

#here's how you access elements of the list
animals = ["bear", "tiger" , "penguin", "zebra"]
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)

print("There are this many thing:", len(random_things))
print("things is a:", type(random_things))

another_list = random_things[-1]
print(another_list)
print(type(another_list))

# Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this:

def city_country(name, country):
  city_and_country = f"{name}, {country}"
  return city_and_country.title()

while True:
  city_name = input("What's the name of the city? ")
  if city_name == 'q':
    break
  country_city = input("What's the city's country? ")
  if country_city == 'q':
    break

  formatted_city_country = city_country(city_name, country_city)
  print(f"\n{formatted_city_country}")


# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return a
# dictionary containing these two pieces of information. Use the function to make three
# dictionaries representing different albums. Print each return value to show that the 
# dictionaries are storing the album information correctly.

# Use None to add an optional parameter to make_album() that allows you to store the number
# of songs on an album. If the calling line includes a value for the number of songs, add 
# that value to the album’s dictionary. Make at least one new function call that includes
# the number of songs on an album.

def make_album(artist, album_title, number_of_songs = None):
  
  if number_of_songs:
    info_album = {
      'artist':artist,
      'title':album_title,
      'songs':number_of_songs,
    }
  else:
    info_album={
      'artist': artist ,
      'title':album_title ,
    } 

  return info_album

# Start with your program from Exercise 8-7. Write a while loop that allows users to enter
# an album’s artist and title. Once you have that information, call make_album() with the 
# user’s input and print the dictionary that’s created. Be sure to include a quit value in 
# the while loop.

while True: 
  artist = input("What is the name of the artist? ")
  if artist == 'q':
    break

  title = input("What's the name of the album? ")
  if title == 'q':
    break

  songs = input("How many songs are in the album? ")
  if songs == 'q':
    break

  album = make_album(artist, title, songs)
  print(album)


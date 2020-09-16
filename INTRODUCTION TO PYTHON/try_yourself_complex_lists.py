guests = ['Guaynaa', 'Katy Perry', 'Orlando Bloom', 'Maluma', 'Miley Cyrus']

for guest in range(0,5):
  print(f"Would you want to come to dinner with me {guests[guest]}")

print('\n')
not_arriving = guests.pop()
new_guest = guests.append('Fuego')


for guest in range(0,5):
  print(f"Would you want to come to dinner with me {guests[guest]}")

for guest in range(0,5):
  print(f"I found a bigger table {guests[guest]}")

guests.insert(0,'Inna')
guests.insert(3,'Farina')
guests.append('Tangana')

for guest in range(0,8):
  print(f"Would you want to come to dinner with me {guests[guest]}")

for guest in range(0,8):
  print(f"I only can invite two people at dinner with me {guests[guest]}")

uninvited = []

for guest in range(0,6): 
  lel=guests.pop()
  uninvited.append(lel)
  print(f"Sorry you are uninvited {lel}")

print(guests)
print(uninvited)

for guest in range(0,2):
  print(f"You are still invited {guests[guest]}")

for guest in range(0,2):
  del guests[guest]

print(guests)


car = 'subaru'

prediction_1 = True

if car == 'subaru':
  print('It\'s a subaru')
else:
  print('It\'s not a subaru')

if car == 'subaru' and prediction_1 == True:
  print('You were right')
else:
  print('You\'re wrong')

if car != 'subaru':
  print('It\'s not a subaru')
else:
  print('It\'s a subaru')

prediction_2 = False

if car == 'audi':
  print('It\'s audi')
else :
  print('It\'s not audi')

if car != 'audi' and prediction_2==False:
  print('You were right')
else:
  print('You were wrong') 

if car != 'audi':
  print('It\'s not an audi')
else:
  print('It\'s a audi')

if car.lower() == 'subaru':
  print('It\'s a subaru')
else:
  print('It\'s not a subaru')
  

car = []
car = ['lexus']
car.append('nissan')

print(car)
if 'lexus' in car:
  print('lexus is in car list')
else:
  print('lexus is not in car list')

if 'honda' not in car:
  print('Honda is not in car')
else:
  print('Honda is on car list')

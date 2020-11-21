
def parity(number):
  """ Make a program that tells us if the number entered by the user is odd or even
  The program will be able to tell if the number has decimals."""
  
  number_f = float(number)
  number_i = round(number_f)
  number_d =number_f-number_i
  
  if number_d == 0 and number_f%2 == 0 :
    print('The number is even!')
  elif number_d == 0 and number_f%2 != 0:
    print('The number is odd!')
  else:
    print('The number has decimals!')


number_1 = input('Tell me a number:')

parity(number_1)
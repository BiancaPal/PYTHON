# Hacer un programa que pida N y dibuje un triángulo como el siguiente de n (=5 en este
# ejemplo) de anchura:

numero = int(input("Introduce un numero: "))

#for i in range(1, numero + 1):
  #print('* ' * i)
#for i in range(1,numero + 1):
  #print('* ' * (numero-i))

doble=numero*2

for i in range(doble):
  if i <= numero:
    print('*' * i)
  else:
    print('*' * (doble-i))

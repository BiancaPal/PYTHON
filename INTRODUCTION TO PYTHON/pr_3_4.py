# Hacer un programa que pida N y dibuje un triángulo como el siguiente de n (=6 en este
# ejemplo) de anchura o altura:

numero = int(input("Introduce un numero: "))

for i in range(numero+1):
  print('*'*i)
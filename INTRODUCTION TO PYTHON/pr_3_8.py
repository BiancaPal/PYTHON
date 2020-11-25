# Hacer un programa que pida N y dibuje un triángulo como el siguiente de n (=6 en este
# ejemplo) de altura:

numero = int(input("Introduce un numero: "))

numero_1 = 1
for i in range(numero+1):
  for j in range(1,i+1):
    print(numero_1, end =' ')

    if numero_1 < 9:
      numero_1 += 1
    else:
      numero_1 = 0
  print()
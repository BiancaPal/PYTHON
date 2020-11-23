# Hacer un programa que pida N y dibuje un triángulo como el siguiente de n (=6 en este
# ejemplo) de altura:

numero = int(input("Introduce un numero: "))

string = [1,2,3,4,5,6,7,8,9,0]

for i in range(0,numero):
  for j in string:
    print(string[j])
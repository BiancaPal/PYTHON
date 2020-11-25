# Hacer un programa que sume con un bucle los cuadrados de los números del 1 al n 
# pidiendo al usuario el valor de n. Después de hacerlo, comprobar que coincide con:
# (n(n + 1)(2n + 1))/6
# Se puede imprimir el resultado de esta ecuación y después el resultado de nuestra 
# suma.

numero = int(input("Introduce un numero:"))
suma = 0
for i in range(1,numero+1):
  cuadrado = i**2
  suma += cuadrado

funcion = (numero*(numero+1)*(2*numero + 1))/6

if suma ==  funcion:
    print("Coincide")
else:
    print("No coincide")
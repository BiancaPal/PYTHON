# Hacer un programa que pida números reales al usuario, hasta que el usuario entre
# el número 0. Después el programa debe imprimir la suma y la media de los números
# positivos, por un lado y la suma y la media de los números negativos, por otro,
# y presentar esos cuatro resultados en la pantalla

import itertools

def media(array_positivos,array_negativos):
  suma_negativos = 0
  suma_positivos = 0
  for n,p in itertools.zip_longest(array_negativos,array_positivos,fillvalue=0):
    suma_negativos += n
    suma_positivos += p
    

  print(f"""La suma de los números negativos es: {suma_negativos} i la media es: 
  {suma_negativos/len(array_negativos)}""")
  print(f"""La suma de los números positivos es: {suma_positivos} i la media es: 
  {suma_positivos/len(array_positivos)}""")

positivos=[]
negativos=[]

while True:
  numero = int(input("Dime un numero: "))
  if numero < 0:
    negativos.append(numero)
  elif numero > 0:
    positivos.append(numero)
  else:
    break

media(positivos,negativos)
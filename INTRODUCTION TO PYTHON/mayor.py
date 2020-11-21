# Hacer un programa que pida tres números y diga el mayor de los tres.
lista=[]
for x in range(3):
  numero = input(f"Disme el número {x}: ")
  lista.append(numero)

numeros_ordenados_desc=sorted(lista,reverse=True)
print(f"El mayor de los 3 és {numeros_ordenados_desc[0]}")

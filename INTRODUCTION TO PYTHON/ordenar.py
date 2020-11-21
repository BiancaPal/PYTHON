# Hacer un programa que pida tres números y los imprima pero ordenadamente. Si le
# damos 8 14 -1, imprimiría -1 8 14

lista=[]
for x in range(3):
  numero = input(f"Disme el número {x}: ")
  lista.append(numero)

numeros_ordenados_desc=sorted(lista)
print(numeros_ordenados_desc)
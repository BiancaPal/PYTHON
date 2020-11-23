# Hacer un programa que pida el lado y pinte un cuadrado hueco como éste: (para n 4)
# * * * *
# *     *
# *     *
# * * * *

numero = int(input("Introduce el numero: "))

for n in range(1,numero+1):
  if n == 1 or n == numero:
    print('* ' *numero)
  else:
    print(f"* "+("  "*(numero-2))+"* ")
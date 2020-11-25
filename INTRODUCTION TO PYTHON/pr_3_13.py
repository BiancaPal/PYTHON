# Hacer un programa que utilizando la librería turtle (import turtle) dibuje un cuadrado de lado
# 100 usando un bucle for de manera que no se tenga que repetir forward(…), left(…) cuatro
# veces sino que sea el bucle for el que repita esta pareja de instrucciones para la tortuga
# (Recordar que las funciones de la tortuga están listadas aquí)

import turtle

for i in range(1,4):
  turtle.forward(100)
  for j in range(1):
    turtle.left(100)

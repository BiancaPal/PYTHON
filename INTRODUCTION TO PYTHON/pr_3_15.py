# Usando un bucle anidado en otro, dibujar la siguiente matriz de x=5 puntos de
# ancho por y=7 puntos de alto separados por sep=25:
# Para hacer un punto podemos usar t.dot()
# Para movernos sin dibujar entre los puntos hacer primero t.penup()

import turtle

t = turtle.Turtle() 

for y in range(1,7+1):
  for x in range(1,5+1):
    t.penup()
    t.dot()
    t.forward(25)
  t.backward(25*5)
  t.right(90) 
  t.forward(25) 
  t.left(90)



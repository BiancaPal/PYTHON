# Repetir el programa anterior pero para dibujar cualquier polígono de lado 50. Para ello
# declaramos una variable nlados=6 (por ejemplo) antes y después repetimos (for) el dibujo del
# lado, y giramos el ánguloExt = 360/nlados, o sea, right(360/nlados).
import turtle

s = turtle.getscreen()

for i in range(1,6):
  turtle.forward(50)
  turtle.left(72)
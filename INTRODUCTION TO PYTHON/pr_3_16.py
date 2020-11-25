# Dibujar con la librería turtle un tablero de ajedrez. Para ello hacer
# cuadrados de longitud lado rellenados de negro en
# las posiciones alternas. Para rellenar de negro un
# cuadrado. Cambiar el ejemplo del Campus (aquí)
# de tal forma que numeremos las filas como en el
# siguiente:


import turtle

t = turtle.Turtle() 
sc = turtle.Screen()


def draw():
  for i in range(4):
    t.forward(30)
    t.left(90)
  t.forward(30)

sc.setup(600, 600)

t.speed(100)

for i in range(8):
  t.up()
  t.setpos(0,30 *i)
  t.down()

  for j in range(8):
    if (i+j)%2 == 0:
      col = 'peru'
    else:
      col = 'burlywood'
    
    t.fillcolor(col)
    t.begin_fill()

    draw()
    t.end_fill()


t.hideturtle()
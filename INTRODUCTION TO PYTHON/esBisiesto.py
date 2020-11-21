# Un año es bisiesto cuando es (1) divisible por 4 pero no por 100 ó (2) divisible por 400.
# Por ejemplo: 2016 es bisiesto; 2000 y 2400 son bisiestos (divisibles por 400), pero 1800,
# 1900, 2100, 2200, 2300 y 2500 no lo son.
# Hacer un programa que pida un número de año (int) y responda si es o no bisiesto.
# Probarlo con los ejemplos propuestos poniendo un mensaje diciendo “Es
# bisiesto” o “No es bisiesto”.

def bisiesto(fecha):
  fecha = int(fecha)
  
  if fecha%400 == 0:
    print("Es bisiesto")
  else:
    print("No es bisiesto")

while True:
  fecha = input("Dime un año, y te diré si és bisiesto o no: ")
  if fecha.upper() != "FIN":
    bisiesto(fecha)
  else:
    break





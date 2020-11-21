def calcular_hipotenusa(a, b):
  """Devolver area del circulo."""
  a_f = float(a)
  b_f = float(b)
  x=-b_f/a_f
  print(f"El resultado de la solución és {x}")

a = input("Dime el coeficiente a: ")
b = input("Dime el coeficiente b: ")

calcular_hipotenusa(a,b)
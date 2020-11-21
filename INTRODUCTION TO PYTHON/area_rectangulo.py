
def calcular_area_rectangulo(altura, base):
  """Devolver area del circulo."""
  altura_f = float(altura)
  base_f = float(base)
  area=base_f*altura_f
  print(area)

altura = input("Dime la altura: ")
base = input("Dime la base: ")

calcular_area_rectangulo(altura, base)
def calcular_area_circulo(radio, pi=3.141492):
  """Devolver area del circulo."""
  radio_int = float(radio)
  area=pi*radio_int**2
  print(area)

radio_string = input("Dime el radio: ")
calcular_area_circulo(radio_string)
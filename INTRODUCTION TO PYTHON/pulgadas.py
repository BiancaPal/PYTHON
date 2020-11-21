def calcular_centimetros(longitud, factor_de_conversion=2.54):
  """Devolver area del circulo."""
  longitud_f = float(longitud)
  longitud_en_cm = longitud_f*factor_de_conversion
  print(longitud_en_cm)

longitud = input("Dime la longitud en pulgadas: ")

calcular_centimetros(longitud)
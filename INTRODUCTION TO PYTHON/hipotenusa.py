import math

def calcular_hipotenusa(cateto_A, cateto_B):
  """Devolver area del circulo."""
  catetoA_f = float(cateto_A)
  catetoB_f = float(cateto_B)
  hipotenusa = math.sqrt((catetoA_f**2)+(catetoB_f**2))
  print(hipotenusa)

catetoA = input("Dime el cateto A: ")
catetoB = input("Dime el cateto B: ")

calcular_hipotenusa(catetoA, catetoB)
# Una fecha (d, m, a) es correcta cuando el día, si es febrero, es menor que 30 en los años
# bisiestos y menor que 29 en los no bisiestos. Los demás meses, dependen del mes, los meses
# enero, marzo, mayo, julio, agosto, octubre y diciembre, tienen 31 días; el resto, 30 Pedir
# al usuario los tres días de una fecha (día, mes y año), y escribir si ES o NO ES fecha 
# válida


def validez(d,m,a):

  [d,m,a]=[int(d),int(m),int(a)]

  meses = [1,2,3,4,5,6,7,8,9,10,11,12]
  
  meses_31 = [1,3,5,7,8,10,11]

  FECHA_VALIDA = f"Fecha válida"
  FECHA_INVALIDA = f"Fecha inválida"

  if m == 2 and d < 30 and a%400 == 0:
    print(FECHA_VALIDA)
  elif m == 2 and d < 29 and a%400 != 0:
    print(FECHA_VALIDA)
  elif m in meses_31 and d <= 31:
    print(FECHA_VALIDA)
  elif m not in meses_31 and m != 2 and m in meses and d <= 30:
    print(FECHA_VALIDA)
  else:
    print(FECHA_INVALIDA)

[d, m, a] = [input("Dime el día: "), input("Dime el mes: "), input("Dime el año: ")]

validez(d,m,a)


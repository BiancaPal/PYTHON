# Hacer un programa que imprima la edad de un perro en "años de perro". Para los primeros
# dos años un año de un perro equivale a 10.5 años humanos. Después, cada año del perro 
# equivale a 4 años humanos. Por ejemplo: Entrar la edad del perro en años humanos: 15.
# La edad del perro en años de perro es: 73

def perro(edad):
  """Intento de conversión de años humano a canino"""
  edad_i = int(edad)+1 
  edad_perro_inicial = 0
  for x in range(edad_i):
    if x == 1 or x == 2:
      edad_perro_inicial = edad_perro_inicial + 10.5
    elif x >= 3:
      edad_perro_inicial = edad_perro_inicial + 4 
  print(edad_perro_inicial)

while True:
  edad = input("Dime una edad humana: ")
  if edad.upper() != "FIN":
    perro(edad)
  else:
    break
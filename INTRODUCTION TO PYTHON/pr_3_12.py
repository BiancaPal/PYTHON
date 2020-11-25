# Un triplete pitagórico (ref) es aquel que cumple: a2=b2+c2 if a*a==b*b+c*c: es triplete
# pitagórico. Pedir un entero n tope al usuario y probar con números a, b y c entre los valores 1
# hasta n. Imprimir los que son tripletes cumplen la ecuación. Hacer un programa que lea n e
# imprima los correspondientes tripletes. Por ejemplo, si n es 20 saldría:

numero = int(input("Introduce un numero: "))

for a in range(1,numero):
  for b in range(1,a):
    for c in range(1,b):
      
      if a**2 == (b**2) + (c**2):
        print(a, b, c)
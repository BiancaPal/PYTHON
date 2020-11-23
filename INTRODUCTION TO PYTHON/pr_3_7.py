# Hacer un programa que pida N y dibuje un triángulo como el siguiente de n (=6 en este
# ejemplo) de altura
# 1
# 12
# 123
# 1234
# 12345
# 123456

numero = int(input("Introduce un numero: "))
string=''
for i in range(1,numero+1):
  string+=str(i)
  print(string)
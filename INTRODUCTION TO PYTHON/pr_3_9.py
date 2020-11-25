# Leer 5 enteros del usuario primero y pintar un histograma con ellos, por ejemplo,
# con 3 0 4 7 2

def  histograma(dictionary):
  
  for key, value in dictionary.items():
    print('*'*value)

dictionary = {}

for i in range (1,6):
  dictionary["numero%s" %i] = int(input("Introduce un numero: "))

histograma(dictionary)
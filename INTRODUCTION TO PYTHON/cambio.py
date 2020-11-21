# Pedir al usuario una cantidad en euros (real) y componer esa cantidad mediante 
# la mínima variedad de billetes y monedas. Para ello pasar primero la cantidad dada
# en euros a céntimos:

def centimos(euros):
  cents = int(euros)
  cents = (round(cents*100))

  factor_conversion = {
    'C500': [50000] ,
    'C200':	[20000] ,		
    'C100':	[10000] ,		
    'C50':	[5000 ],
    'C20':	[2000 ],
    'C10':	[1000 ],
    'C5':	[500] ,
    'C2':	[200] ,	
    'C1':	[100] ,	
    'C050':	[50] ,
    'C020':	[20] ,
    'C010':	[10] ,
    'C005':	[5 ],
    'C002':	[2 ],
    'C001':	[1 ], 
  }
  numero_billetes_por_billete = {}
  for key,value in factor_conversion.items():
    for numero in value:
      if cents >= numero:
        numero_billetes = cents // numero 
        numero_billetes_por_billete.update({key:numero_billetes})
        cents_convertidos = numero * numero_billetes
        cents = cents - cents_convertidos
      else:
        numero_billetes_por_billete.update({key:0})
  
  print(numero_billetes_por_billete) 


euros= input("Dime los euros: ")
centimos(euros)

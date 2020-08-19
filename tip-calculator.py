total_amount = input("How much is the total amount? ")
total_amount_int = int(total_amount.replace("$", " "))

tip_15 = total_amount_int*0.15
tip_18 = total_amount_int*0.18
tip_20 = total_amount_int*0.20
print (f"A 15% tip would be an amount of ${tip_15:.2f}")
print (f"A 18% tip would be an amount of ${tip_18:.2f}")
print (f"A 20% tip would be an amount of ${tip_20:.2f}")
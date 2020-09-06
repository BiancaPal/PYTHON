#strings are text sorrounded by quotes
#both single (') or double  (") or triple (""") quotes are used
# examples: "dinosaurs", "2112" , "I'm lovin' it"

kanye_quote = """My greatest pain in life
is that I will never be able 
to see myself perform live."""

print (kanye_quote)

hamilton_quote = 'Well, the word got around, they said, "This kid\'s insane, man"'

print(hamilton_quote)

name = "Bianca Maria Pal"
orphan_fee = 200
teddy_bear_fee = 121.80

total = orphan_fee + teddy_bear_fee

#print(name, "the total will be", total)
print(f"{name} the total will be ${total:.2f}")
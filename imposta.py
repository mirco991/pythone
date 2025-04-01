reddito = input("Quale è il tuo reddito?")
red=int(reddito)

if red<28000 : print("La tua imposta è: ", 28000/100*23)
if 28000<red<50000 : print("La tua imposta è: ", (28000/100*23)+(22000/100*35))
##if red>50000 : print("La tua imposta è: ",(red)/100*43)

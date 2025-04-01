somma=0
numeri_letti=0
numero= input("Passami il prossimo valore oppure 'exit' per uscire dal programma: ")
while numero!= "exit" :
    somma+=int(numero)
    numeri_letti+=1
    numero= input("Passami il prossimo valore oppure 'exit' per uscire dal programma: ")

print("La media dei numeri letti è ", somma/numeri_letti)

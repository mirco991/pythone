carattere = input("Quale carattere devo utilizzare?")
ampiezza = int(input("Quanto deve essere grande l'ampiezza dell'albero?"))

i= 1
while i <= ampiezza :
    print(" " * ((ampiezza-i)//2)+carattere*i)
    i+=2

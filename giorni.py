GIORNI=("Lunedì   " +
        "Martedì  " +
        "Mercoledì" +
        "Giovedì  " +
        "Venerdì  " +
        "Sabato   " +
        "Domenica ")
giorno = int(input("Indica giorno: "))
p= (giorno -1) * 9
print(GIORNI[p] + GIORNI[p+1] + GIORNI[p+2] + GIORNI[p+3] + GIORNI[p+4] + GIORNI[p+5] + GIORNI[p+6])

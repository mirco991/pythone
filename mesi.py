MESI=   ("Gennaio  " +
        "Febbraio " +
        "Marzo    " +
        "Aprile   " +
        "Maggio   " +
        "Giugno   " +
        "Luglio   " +
        "Agosto   " +
        "Settembre" +
        "Ottobre  " +
        "Novembre " +
        "Dicembre ")
mese = int(input("Indica mese: "))
p= (mese -1) * 9
print(MESI[p] + MESI[p+1] + MESI[p+2] + MESI[p+3] + MESI[p+4] + MESI[p+5] + MESI[p+6] + MESI[p+7] + MESI[p+8])

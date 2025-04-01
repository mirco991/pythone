reddito = int(input("Quale è il tuo reddito?"))
ALIQUOTA_1 = 0.23
ALIQUOTA_2 = 0.35
ALIQUOTA_3 = 0.43
SCAGLIONE_1 = 28000
SCAGLIONE_2 = 50000

if reddito<=SCAGLIONE_1 : print("La tua imposta è: ", (reddito)*(ALIQUOTA_1))
if reddito > SCAGLIONE_1 and reddito <= SCAGLIONE_2 : print("La tua imposta è: ", ((SCAGLIONE_1*ALIQUOTA_1)+ ((reddito - SCAGLIONE_1) *ALIQUOTA_2)))
else : print("La tua imposta è: ", SCAGLIONE_1 * ALIQUOTA_1 + ((SCAGLIONE_2 - SCAGLIONE_1) * ALIQUOTA_1) + ((reddito - SCAGLIONE_2) * ALIQUOTA_3))

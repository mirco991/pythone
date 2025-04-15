import math

class SodaCan:
    def __init__(self, altezza, raggio):
        self._altezza = altezza
        self._raggio = raggio

    def getSurfaceArea(self):
        circonferenza = 2 * math.pi * self._raggio**2
        laterale = 2 * math.pi * self._raggio * self._altezza
        return circonferenza + laterale

    def getVolume(self):
        return math.pi * self._raggio**2 * self._altezza

mini_lattina = SodaCan(7.6, 2.5)
lattina = SodaCan(9.24, 3.37)
print("Mini lattina:")
print("Superficie:", mini_lattina.getSurfaceArea())
print("Volume:", mini_lattina.getVolume())
print("Lattina:")
print("Superficie:", lattina.getSurfaceArea())
print("Volume:", lattina.getVolume())

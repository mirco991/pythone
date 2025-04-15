class Letter:
    def __init__(self, letterFrom, letterTo):
        self.letterFrom = letterFrom
        self.letterTo = letterTo
        self.content = ""
    
    def addLine(self, line):
        self.content += line + "\n"

    def getText(self):
        letter_text = f"Dear {self.letterTo},\n\n"
        for line in self.content:
            letter_text += line
        letter_text += "\nSincerely,\n\n" + self.letterFrom
        return letter_text
    
lettera = Letter("Mary", "John")
lettera.addLine("Spero tu stia bene")
lettera.addLine("Volevo chiederti se hai ricevuto la mia ultima email.")
lettera.addLine("Fammi sapere quando hai un momento.")
print(lettera.getText())

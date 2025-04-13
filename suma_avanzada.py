class SumaAvanzada():
    def __init__(self, nveces):
        self.nveces = nveces

    def sumar(self):
        self.resultado = 0
        for i in range(self.nveces):

            try:
                number = int(input("Ingresa el numero que deseas sumar: ")) 
            except ValueError:
                return "No es un numero" 

            self.resultado += number

        return self.resultado



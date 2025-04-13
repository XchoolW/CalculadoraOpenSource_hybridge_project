class Suma():
    
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def sumar(self):
        try:
            self.result = self.n1 + self.n2
        except ValueEror:
            return "No es un numero"

        return self.result

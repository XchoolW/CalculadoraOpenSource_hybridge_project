class Dividir():
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def dividir(self):
        try:
            self.result = self.n1 / self.n2
        except ZeroDivisionError:
            return "No se puede dividir entre 0"
        
        return self.result

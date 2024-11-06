"""Modulo 1: Clase en Python que guarda un valor entero"""
class Modulo1:
    valor = 0

    """Inicializa la clase Modulo1"""
    def __init__(self,valor):
        self.valor = valor

    """"Imprime la clase Modulo1"""
    def printValor(self):
        print("Modulo 1: " + str(self.valor))

    def getValor(self):
        return self.valor


if __name__ == '__main__':
    modulo = Modulo1(18)
    modulo.printValor()

import os


class CalcularDobroTriplo:
    dobro:int
    triplo:int
    def __init__(self, numero):
        self.numero = numero
    
    def calcularVariaveis(self):
        self.dobro = self.numero * 2
        self.triplo = self.numero * 3
        
    def __repr__(self):
        return f"O número é {self.numero} seu dobro é {self.dobro} e seu triplo é {self.triplo}"
    
if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de cálculo do dobro e triplo de um número!\n")
        numero = int(input("Digite o número:\n"))
        os.system('cls')
        dobroTriplo = CalcularDobroTriplo(numero)
        dobroTriplo.calcularVariaveis()
        print(dobroTriplo)
    except Exception as err:
        print(f"\nValor digitado incorreto!")
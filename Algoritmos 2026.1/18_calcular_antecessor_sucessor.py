import os


class CalcularAntecessorSucessor:
    antecessor:int
    sucessor:int
    def __init__(self, numero):
        self.numero = numero
    
    def calcularVariaveis(self):
        self.antecessor = self.numero - 1
        self.sucessor = self.numero + 1
        
    def __repr__(self):
        return f"O número é {self.numero} seu antecessor é {self.antecessor} e seu sucessor é {self.sucessor}"
    
if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de cálculo do antecessor e sucessor de um número!\n")
        numero = int(input("Digite o número:\n"))
        os.system('cls')
        antecessorSucessor = CalcularAntecessorSucessor(numero)
        antecessorSucessor.calcularVariaveis()
        print(antecessorSucessor)
    except Exception as err:
        print(f"\nValor digitado incorreto!")
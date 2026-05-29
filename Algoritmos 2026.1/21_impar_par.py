import os

class VerificarSeNegativoPositivo:
    ehImpar: bool
    def __init__(self, numero):
        self.numero = numero
    
    def verificarSeNegativoPositivo(self):
        if numero % 2 == 1:
            self.ehImpar = True
        else:
            self.ehImpar = False
        
    def __repr__(self):
        return f"O número é {self.numero} e ele é {"Impar" if self.ehImpar else "Par"}"
    
if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de verificar impar par!\n")
        numero = int(input("Digite o número:\n"))
        os.system('cls')
        seNegativoPositivo = VerificarSeNegativoPositivo(numero)
        seNegativoPositivo.verificarSeNegativoPositivo()
        print(seNegativoPositivo)
    except Exception as err:
        print(f"\nValor digitado incorreto!")
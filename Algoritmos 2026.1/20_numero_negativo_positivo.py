import os

class VerificarSeNegativoPositivo:
    ehNegativo: bool
    def __init__(self, numero):
        self.numero = numero
    
    def verificarSeNegativoPositivo(self):
        if numero < 0:
            self.ehNegativo = True
        elif numero > 0:
            self.ehNegativo = False
        
    def __repr__(self):
        return f"O número é {self.numero} e ele é {"Negativo" if self.ehNegativo else "Positivo"}" if numero != 0 else "O número é 0 e ele é Neutro"
    
if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de verificar negativo positivo!\n")
        numero = float(input("Digite o número   :\n"))
        os.system('cls')
        seNegativoPositivo = VerificarSeNegativoPositivo(numero)
        seNegativoPositivo.verificarSeNegativoPositivo()
        print(seNegativoPositivo)
    except Exception as err:
        print(f"\nValor digitado incorreto!")
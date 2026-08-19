import os

class VerificarQualMaior:
    maiorNumero: int
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero1 = numero2
    
    def verificarQualMaior(self):
        if numero1 > numero2:
            self.maiorNumero = numero1
        elif numero1 < numero2:
            self.maiorNumero = numero2
        else:
            self.maiorNumero = numero1
        
    def __repr__(self):
        return f"O maior número inteiro é {self.maiorNumero}"
    
if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de verificar qual é maior!\n")
        numero1 = int(input("Digite o primeiro número:\n"))
        numero2 = int(input("Digite o segundo número:\n"))
        os.system('cls')
        verificarQualMaior = VerificarQualMaior(numero1, numero2)
        verificarQualMaior.verificarQualMaior()
        print(verificarQualMaior)
    except Exception as err:
        print(f"\nValor digitado incorreto!")
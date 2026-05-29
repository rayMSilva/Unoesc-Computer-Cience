import os


class OperacoesMatematicas:
    numero1: float
    numero2: float
    soma: float
    subtracao: float
    divisao: float
    multiplicacao: float
    dividir: float
    
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
    def somar(self):
        self.soma = self.numero1 + self.numero2
        
    def subtrair(self):
        self.subtracao = self.numero1 - self.numero2
        
    def dividir(self):
        self.divisao = self.numero1 / self.numero2
        
    def multiplicar(self):
        self.multiplicacao = self.numero1 * self.numero2

    
if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de operações matemáticas!\n")
        num1 = float(input("Digite o 1° número:\n"))
        num2 = float(input("Digite o 2° número:\n"))
        os.system('cls')
        operacoes = OperacoesMatematicas(num1, num2)
        operacoes.somar()
        operacoes.dividir()
        operacoes.subtrair()
        operacoes.multiplicar()
        print(f"Soma: {operacoes.soma:.2f}")
        print(f"Subtração: {operacoes.subtracao:.2f}")
        print(f"Divisão: {operacoes.divisao:.2f}")
        print(f"Multiplicação:{operacoes.multiplicacao:.2f}")
    except Exception as err:
        print(f"\nValor digitado incorreto!")
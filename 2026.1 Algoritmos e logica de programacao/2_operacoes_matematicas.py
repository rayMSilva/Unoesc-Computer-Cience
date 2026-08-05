import os


class OperacoesMatematicas:
    numero1: float
    numero2: float
    soma: float
    subtracao: float
    divisao: float
    multiplicacao: float
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
        
    def __repr__(self):
        return f'''Resultado das operações:
Soma: {self.soma:.2f}
Subtração: {self.subtracao:.2f}
Multiplicação: {self.multiplicacao:.2f}
Divisão: {self.divisao:.2f}\n'''
    
if __name__ == "__main__":
    try:
        os.system("cls")
        print("Bem-vindo ao sistema de operações matemáticas!\n")
        num1 = float(input("Digite o 1° número:\n"))
        num2 = float(input("Digite o 2° número:\n"))
        os.system("cls")
        operacoes = OperacoesMatematicas(num1, num2)
        operacoes.somar()
        operacoes.dividir()
        operacoes.subtrair()
        operacoes.multiplicar()
        print(operacoes)
    except Exception as err:
        print("\nValor digitado incorreto!")
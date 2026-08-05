import os


class Operacao:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def somarDoisNumeros(self):
        return self.num1 + self.num2
    
if __name__ == "__main__":
    try:
        os.system("cls")
        print("Bem-vindo ao sistema de soma!\n")
        num1 = float(input("Digite o 1° número:\n"))
        num2 = float(input("Digite o 2° número:\n"))
        os.system("cls")
        soma = Operacao(num1, num2).somarDoisNumeros()
        print(f'''Resultado das operações:
Soma: {soma:.2f}''')
    except Exception as err:
        print("\nValor digitado incorreto!")
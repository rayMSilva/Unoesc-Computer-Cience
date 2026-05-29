import os


class Media:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def mediaEntreDoisNumeros(self):
        return (self.num1 + self.num2) / 2
    
if __name__ == "__main__":
    try:
        os.system("cls")
        print("Bem-vindo ao sistema de média!\n")
        num1 = float(input("Digite o 1° número:\n"))
        num2 = float(input("Digite o 2° número:\n"))
        os.system("cls")
        media = Media(num1, num2).mediaEntreDoisNumeros()
        print(f'''Resultado das operações:
Média: {media:.2f}''')
    except Exception as err:
        print("\nValor digitado incorreto!")
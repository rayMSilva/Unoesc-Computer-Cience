import os


class VerificarMaiorIdade:
    def __init__(self, idade):
        self.idade = idade
    
    def verificarIdadeEImprimir(self):
        ehMaior = self.idade > 18
        if (ehMaior):
            print("\n\n\nO usuário é maior de idade\n\n\n")
        else:
            print("\n\n\nO usuário não é maior de idade\n\n\n")
            
if __name__ == "__main__":
    try:
        os.system("cls")
        print("Bem-vindo ao sistema de verificação de idade!\n")
        idade = int(input("Digite a idade do usuário:\n"))
        os.system("cls")
        verificarIdade = VerificarMaiorIdade(idade)
        verificarIdade.verificarIdadeEImprimir()
    except Exception as err:
        print("\nValor digitado incorreto!")
    
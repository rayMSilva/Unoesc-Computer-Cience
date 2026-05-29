import os
from time import sleep
           
class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def __repr__(self):
        return f"Aluno Nome: {self.nome}\nIdade: {self.idade}\nCurso: {self.curso}"
    
    
if __name__ == "__main__":
    try:
        os.system("cls")
        print("Bem-vindo ao sistema de cadastro acadêmico!\n")
        nome = str(input("Digite o nome do Aluno:\n"))
        idade = int(input("Digite a idade do Aluno:\n"))
        curso = str(input("Digite o curso do Aluno:\n"))
        aluno = Aluno(nome, idade, curso)
        os.system('cls')
        print("Processando cadastro!")
        print("...\n\n")
        sleep(2)
        print(aluno)
    except Exception as err:
        print("\nValor digitado incorreto!")
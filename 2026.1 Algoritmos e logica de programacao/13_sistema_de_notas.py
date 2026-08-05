import os
from time import sleep
           
class Aluno:
    media:float
    situacao:bool
    
    def __init__(self, nome, idade, curso, nota1, nota2, nota3):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def calcularMedia(self):
        self.media = (self.nota1 + self.nota2 + self.nota3) / 3
        
    def verificarAprovacao(self):
        if self.media < 6:
            self.situacao = False
        else:
            self.situacao = True
    
    
    def __repr__(self):
        return f"Aluno Nome: {self.nome}\nIdade: {self.idade}\nCurso: {self.curso}\nSituação: {"Aprovado" if self.situacao == True else "Reprovado"}\nMédia: {self.media:.2f}"
    
    
if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de cadastro acadêmico!\n")
        nome = str(input("Digite o nome do Aluno:\n"))
        idade = int(input("Digite a idade do Aluno:\n"))
        curso = str(input("Digite o curso do Aluno:\n"))
        nota1 = float(input("Digite 1° nota do usuário:\n"))
        nota2 = float(input("Digite 2° nota do usuário:\n"))
        nota3 = float(input("Digite 3° nota do usuário:\n"))
        os.system('cls')
        aluno = Aluno(nome, idade, curso, nota1, nota2, nota3)
        aluno.calcularMedia()
        aluno.verificarAprovacao()
        print("Listando caracteristicas!")
        print("...\n\n")
        sleep(2)
        print(aluno)
    except Exception as err:
        print("\nValor digitado incorreto!")
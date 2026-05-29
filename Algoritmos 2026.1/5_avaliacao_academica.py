import os


class AvaliacaoMediaAcademica:
    
    def __init__(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        
    def calcularMedia(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
        
    def verificarAprovacaoEImprimir(self, media):
        if media < 6:
            print(f"Aluno Reprovado! Média final: {media:.2f}")
        else:
            print(f"Aluno Aprovado! Média final: {media:.2f}")


if __name__ == "__main__":
    try:
        os.system("cls")
        print("Bem-vindo ao sistema de verificação de notas!\n")
        nota1 = int(input("Digite 1° nota do usuário:\n"))
        nota2 = int(input("Digite 2° nota do usuário:\n"))
        nota3 = int(input("Digite 3° nota do usuário:\n"))
        os.system("cls")
        if nota1 <= 10 or nota2 <= 10 or nota3 <= 10:
            aprovacao = AvaliacaoMediaAcademica(nota1, nota2, nota3)
            media = aprovacao.calcularMedia()
            aprovacao.verificarAprovacaoEImprimir(media)
        else: 
            print("foi encontrado uma nota acima de 10, isso não é possível!")
    except Exception as err:
        print("\nValor digitado incorreto!")
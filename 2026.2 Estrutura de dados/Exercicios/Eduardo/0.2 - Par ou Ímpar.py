#Função
def ParImpar(valor):
    if valor % 2 == 0:
        return "par"
    else:
        return "ímpar"
#Input do valot inteiro
valor = int(input("Informe sua idade!\n"))

print(f"Você sabia que sua idade é um número {ParImpar(valor)}?\nE sabe o que isso significa? NADA")


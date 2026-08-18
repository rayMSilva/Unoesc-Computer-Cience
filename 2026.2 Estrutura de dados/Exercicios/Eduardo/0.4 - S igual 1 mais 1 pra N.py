S = []
N = 1

def Calculo(S,N):
    S.append(1/N)

Valor = int(input("Digite um número inteiro positivo\n"))

while N != Valor:
    Calculo(S,N)
    N += 1

print(sum(S))
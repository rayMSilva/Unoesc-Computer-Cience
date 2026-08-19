s = []
n = 1

def calculo(s,n):
    s.append(1/n)

valor = int(input("Digite um número inteiro positivo\n"))

while n != valor:
    calculo(s,n)
    n += 1

print(sum(s))
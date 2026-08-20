def cadastrarVetor(vetor, qtdElementos):
    for i in range(qtdElementos):
        while(True):
            try:
                vetor[i] = int(input(f"Digite o valor inteiro da posição V[{i}]:\n"))
                break
            except ValueError:
                print("valor digitado precisa ser um inteiro! Digite novamente\n")
            except Exception:
                print("erro. Digite novamente\n")
                
def somarVetor(vetor, qtdElementos):
    soma = 0
    for i in range(qtdElementos):
        soma += vetor[i]
    return soma

def buscar(vetor, qtdElementos, pesquisa):
    for i in range(qtdElementos):
        if (pesquisa == vetor[i]):
            return i
    return -1

def inverter(vetor, qtdElementos):
    for i in range(qtdElementos):
        for j in range(qtdElementos):
            if i + j == qtdElementos - 1 and i < j:
                a1 = vetor[i]
                a2 = vetor[j]
                vetor[i] = a2
                vetor[j] = a1
                
def bbSort(vetor, qtdElementos):
    for i in range(qtdElementos):
        for j in range(qtdElementos):
            a1 = vetor[i]
            a2 = vetor[j]
            if a1 < a2:
                vetor[i] = a2
                vetor[j] = a1
                
def maiorEPosicao(vetor, qtdElementos):
    maior = vetor[0]
    posicao = 0
    for i in range(qtdElementos):
        if vetor[i] > maior:
            maior = vetor[i]
            posicao = i
    return maior, posicao

def mostrarVetor(vetor, elementos):
    for i in range(elementos):
        print(f"posição V[{i}]: valor {vetor[i]}" if i != elementos - 1 else f"posição V[{i}]: valor {vetor[i]}\n\n")
    
                
if __name__ == "__main__":
    vetor = [0] * 10
    print(f"Bem vindo ao sistema de gerenciamento de vetores!")
    print(f"Para sair do sistema use CTRL + C!!\n\n")
    try:
        cadastrarVetor(vetor, 10)
        bbSort(vetor, 10)
        inverter(vetor,10)
        mostrarVetor(vetor, 10)
        soma = somarVetor(vetor, 10)
        print(f"A soma de todos os valores do vetor cadastrado é {soma}\n")
        print(f"Buscando valor 9\n")
        print(f"Valor 9 encontrado no vetor" if buscar(vetor,10,9) != -1 else "Valor 9 não encontrado no vetor\n")
        print(f"Invertendo vetor\n")
        inverter(vetor,10)
        mostrarVetor(vetor,10)
        print(f"Buscando maior valor\n")
        maior, posicao = maiorEPosicao(vetor, 10)
        print(f"o maior valor é {maior} e sua poição é {posicao}\n")
    except KeyboardInterrupt:
        print("Obrigado por utilizar o sistema!\n")
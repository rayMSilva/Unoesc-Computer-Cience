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
    
def mostrarVetor(vetor, elementos):
    for i in range(elementos):
        print(f"posição V[{i}]: valor {vetor[i]}" if i != elementos - 1 else f"posição V[{i}]: valor {vetor[i]}\n\n")

def AlterarVetor(vetor, elementos, procurado, novoValor):
    alteracoes = 0
    for i in range(elementos):
        if (vetor[i] == procurado):
            vetor[i] = novoValor
            alteracoes+=1
    return alteracoes
    

if __name__ == "__main__":
    vetor = [0] * 10
    print(f"Bem vindo ao sistema de gerenciamento de vetores!")
    print(f"Para sair do sistema use CTRL + C!!\n\n")
    try:
        cadastrarVetor(vetor, 10)
        mostrarVetor(vetor, 10)
        totalAlterado = AlterarVetor(vetor, 10, 9, -1)
        mostrarVetor(vetor, 10)
        if (totalAlterado > 0):
            print(f"Elementos alterados com sucesso, foram alteradas {totalAlterado} poisições!")
        elif (totalAlterado<=0):
            print("O valor não foi enccontrado. Nenhuma posição foi alterada!")
    except KeyboardInterrupt:
        print("Obrigado por utilizar o sistema!\n")
    
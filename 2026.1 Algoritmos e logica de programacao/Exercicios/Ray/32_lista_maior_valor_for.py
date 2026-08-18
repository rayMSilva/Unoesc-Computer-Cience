if __name__ == "__main__":
    try:
        lista = []
        print("Digite 5 números para formar uma lista e vou exibir o maior valor\n")
        for i in range(0,5):
            saida = 0
            saida = float(input("digite um número para ser incrementado á lista de números:\n"))
            lista.append(saida)
        listaCompleta = " , ".join(str(n) for n in lista)
        maiorValor  = max(lista)
        print(f"Os número são da lista são: {listaCompleta}")
        print(f"O maior número é: {maiorValor}")
    except Exception as e:
        print("error")
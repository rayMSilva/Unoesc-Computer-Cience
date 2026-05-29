if __name__ == "__main__":
    try:
        lista = []
        print("Digite 5 números para formar uma lista e vou exibir a quantidade de númerosnegativos presentes nela\n")
        for i in range(0,5):
            saida = 0
            saida = float(input("digite um número para ser incrementado á lista de números:\n"))
            lista.append(saida)
        listaCompleta = " , ".join(str(n) for n in lista)
        quantidadeNumerosNegativos  = sum(1 for i in lista if i<0)
        print(f"Os número são da lista são: {listaCompleta}")
        print(f"A quantidade de números negativos é: {quantidadeNumerosNegativos}")
    except Exception as e:
        print("error")
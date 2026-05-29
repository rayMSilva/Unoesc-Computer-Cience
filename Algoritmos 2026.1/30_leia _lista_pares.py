if __name__ == "__main__":
    try:
        lista = []
        print("Digite 5 números para formar uma lista e vou exibir a lista apenas de números pares\n")
        for i in range(0,5):
            saida = 0
            saida = float(input("digite um número para ser incrementado á lista de números:\n"))
            lista.append(saida)
        listaCompleta = " , ".join(str(n) for n in lista)
        listaPares = " ,".join(str(n) for n in lista if n % 2 == 0)
        print(f"Os número são da lista são: {listaCompleta}")
        print(f"Os números pares são: {listaPares}")
    except Exception as e:
        print("error")
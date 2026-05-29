if __name__ == "__main__":
    try:
        lista = []
        for i in range(0,5):
            saida = 0
            saida = float(input("digite um número para ser incrementado á lista de números:\n"))
            lista.append(saida)
        resultado = " , ".join(str(n) for n in lista)
        print(f"Os número são: {resultado}")
    except Exception as e:
        print("error")
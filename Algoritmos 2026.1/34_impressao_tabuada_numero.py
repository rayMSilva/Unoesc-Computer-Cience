if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro maior que 1 e eu direi sua tabuada de 1 a 10:\n"))
        for i in range(1,11):
            print(f"{numero} * {i} = {numero*i}\n")
    except Exception as e:
        print("Error")
if __name__ == "__main__":
    try:
        soma = 0
        leitura = None
        while leitura != 0:
            leitura = None
            leitura = float(input("Digite um número para ser somado e caso queira sair do loop digite 0!\n"))
            if leitura != 0:
                soma+=leitura
        print(f"\nA soma dos números digitados é: {soma}")
    except Exception as e:
        print("error")
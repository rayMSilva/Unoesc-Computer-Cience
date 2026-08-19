def calcularGorjeta(valor: float, taxa: float):
    if (valor > 0):
        taxaDeGarcom = valor * (taxa/100)
        print(f"""\n\n{"*" * 20} Conta restaurante {"*" * 20}
consumo no restaurante: {valor:.2f}
taxa de garçom: {taxaDeGarcom:.2f}
total: {valor + taxaDeGarcom:.2f}\n\n""")
    else:
        print("O valor informado deve ser maior do que 0")




if __name__ == "__main__":
    print("Bem vindo ao sistema de definição gorjeta\n")
    while(True):
        try:
            valorConta = float(input("Digite o valor consumido no restaurante ao total ou CTRL + C para SAIR!!\n"))
            calcularGorjeta(valorConta, 5)
        except KeyboardInterrupt:
            print("Obrigado por utilizar o sistema!\n")
            break
        except Exception:
            print("erro de digitação\n")
            continue
def calcularProgressao(n):
        soma = 0
        for i in range(1,n+1):
            soma += 1.0/i
    
        return soma


if __name__ == "__main__":
    valor = 0
    while (True): 
        try:
            valor = int(input("Digite um valor inteiro e eu irei calcular sua progressao ou CTRL + C para SAIR!!\n"))
            if valor > 0:
                resultado = calcularProgressao(valor)
                print(f"O valor final é {resultado:.2f}\n\n")
            else:
                print(f"O valor deve ser maior que zero!\n\n")
        except ValueError as e:
            print(f"O valor deve ser um número inteiro")
            continue
        except KeyboardInterrupt:
            print("Obrigado pela atenção!!!\n\n")
            break
        except Exception as e:
            print("Erro")
            continue
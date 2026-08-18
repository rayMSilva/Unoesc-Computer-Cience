class DefinirParOuImpar:
    def ehPar(self, valor):
        return valor % 2 == 0
    
    
if __name__ == "__main__":
    print("Bem vindo ao sistema de definição de pares ou impares\n")
    parOuImpar = DefinirParOuImpar()
    while(True):
        try:
            valor = int(input("Digite o valor inteiro e eu definirei se o valor é par ou impar ou CTRL + C para SAIR!!\n"))
            if parOuImpar.ehPar(valor):
                print("O valor digitado é par\n")
            elif not parOuImpar.ehPar(valor):
                print("O valor Digitado é ímpar\n")
            else:
                print("O valor não foi reconhecido\n")
        except KeyboardInterrupt:
            print("Obrigado por utilizar o sistema!\n")
            break
        except Exception:
            print("erro de digitação\n")
            continue
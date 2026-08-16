class Conversao:
    def converterReaisParaDolares(self, reais, cotacao):
        return reais / cotacao
    
    def converterDolaresParaReais(self, dolares, cotacao):
        return dolares * cotacao
    
    def mostrarValorConvertido(self, valor, ehDolaresParaReais):
        print(f"O valor final da conversão de dólares para reais é {valor:.2f}\n" if ehDolaresParaReais else f"O valor final da conversão de reais para dólares é {valor:.2f}\n")
        
if __name__ == "__main__":
    conversao = Conversao()
    print(f"Bem vindo ao sistema de conversão de dólares e reais\n") 
    while(True):
        try:
            valor = 0
            valor = float(input(f"Digite o valor que deseja converter pode ser em reais ou em dólares ou CTRL + C para SAIR!!!\n"))
            operacao = input(f"Digite o tipo de conversão que deseja realizar (1) U$ => R$ (2) R$ => U$\n")
            if operacao == "1":
                resultado = conversao.converterDolaresParaReais(valor, 5.20)
                conversao.mostrarValorConvertido(resultado, True)
            elif operacao == "2":
                resultado = conversao.converterReaisParaDolares(valor, 5.20)
                conversao.mostrarValorConvertido(resultado, False)
            else:
                input(f"Operação de conversão indevida!\n")
        except KeyboardInterrupt:
            print(f"Obrigado por utilizar o nosso sistema de conversão!\n")
            break
        except Exception as e:
            print(f"Erro de inserção de valores.\n")
            continue
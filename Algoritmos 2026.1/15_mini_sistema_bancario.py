import os


class MiniSistemaBancario:
    def __init__(self, valorInicial):
        self.valorTotal = valorInicial
        
    def sacar(self, valor):
        if (self.valorTotal - valor) > 0:
            self.valorTotal -= valor
        else:
            print("Você não possui saldo suficiente!\n")
            
    def depositar(self, valor):
        self.valorTotal += valor
        
    def mostrarSaldo(self):
        return f"""\nResumo Saldo Bancário:
Saldo Total: R${self.valorTotal:.2f}\n"""

if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao mini sistema bancário!\n")
        valorInicial = float(input("Digite o valor inicial da conta!\n"))
        banco = MiniSistemaBancario(valorInicial)
        while True:
            usarSistema = str(input("Você gostaria de utilizar o sistema bancário? Y/N\n"))
            usarSistema = usarSistema.strip()
            usarSistema = usarSistema.lower()
            os.system('cls')
            if usarSistema == "n":
                print("Encerrando...\n")
                break
            elif usarSistema != "y":
                print("Opção Errada...\n")
                continue
            operacao = str(input("O que você deseja fazer D(depositar)/S(sacar)/M(mostrar/Saldo)\n"))
            operacao = operacao.strip()
            operacao = operacao.lower()
            match operacao:
                case "d":
                    deposito = float(input("Digite o valor do deposito\n"))
                    banco.depositar(deposito)
                case "s":
                    saque = float(input("Digite o valor do saque\n"))
                    banco.sacar(saque)
                case "m":
                    print(banco.mostrarSaldo())
                case _:
                    print("Opção Errada...\n")
    except Exception as e:
        print(f"Valor indevido")
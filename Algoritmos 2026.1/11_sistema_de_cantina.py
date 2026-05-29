import os


class SistemaDeCantina:
    valorTotal:float
    valorDescontoAplicado:float
    def __init__(self, preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade
    
    def calcularValorTotal(self):
        self.valorTotal =  self.preco * quantidade

    def aplicarDescontoProduto(self):
        self.valorDescontoAplicado =  self.valorTotal * 0.90

if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de cálculo do produto na cantina!\n")
        valor = float(input("Digite o valor do Produto:\n"))
        quantidade = float(input("Digite a quantidade do Produto:\n"))
        totalPedidoCantina = SistemaDeCantina(valor, quantidade)
        os.system('cls')
        totalPedidoCantina.calcularValorTotal()
        totalPedidoCantina.aplicarDescontoProduto()
        print(f"Valor Total: {totalPedidoCantina.valorTotal}")
        print(f"Desconto Aplicado: {totalPedidoCantina.valorDescontoAplicado}")
    except Exception as err:
        print(f"\nValor digitado incorreto!")
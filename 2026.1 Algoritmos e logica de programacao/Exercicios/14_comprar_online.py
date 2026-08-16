import os


class SistemaDeCompras:
    valorTotal: float
    valorTotalDescontoAplicado: float
    def __init__(self, preco, quantidade):
        self.preco = preco
        self.quantidade = quantidade
    
    def calcularValorTotal(self):
        self.valorTotal = self.preco * quantidade

    def aplicarDescontoProduto(self):
        self.valorTotalDescontoAplicado =   self.valorTotal * 0.90

if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de cálculo do valor final produto!\n")
        valor = float(input("Digite o valor do Produto:\n"))
        quantidade = float(input("Digite a quantidade do Produto:\n"))
        os.system('cls')
        totalPedidoCantina = SistemaDeCompras(valor, quantidade)
        totalPedidoCantina.calcularValorTotal()
        totalPedidoCantina.aplicarDescontoProduto()
        print(f"Valor Total:  {totalPedidoCantina.valorTotal:.2f}")
        print(f"Desconto Aplicado:  {totalPedidoCantina.descontoAplicado:.2f}")
    except Exception as err:
        print(f"\nValor digitado incorreto!")
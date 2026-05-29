import os


class FolhaDePagamento:
    salarioBruto: float
    salarioLiquido: float
    def __init__(self, valorHora, quantidadeHoras, valorDesconto):
        self.valorHora = valorHora
        self.quantidadeHoras = quantidadeHoras
        self.valorDesconto = valorDesconto
    
    def calcularSalarioBruto(self):
        self.salarioBruto = self.valorHora * self.quantidadeHoras

    def aplicarDescontoFolhaPagamento(self):
        self.salarioLiquido =  self.salarioBruto * (1- (self.valorDesconto / 100))

if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de cálculo de folha de pagamento ntina!\n")
        valorHora = float(input("Digite o valor da hora trabalhada:\n"))
        quantidadeHora = float(input("Digite quantidade de horas trabalhadas:\n"))
        valorDesconto = float(input("Digite o desconto total do salário:\n"))
        os.system('cls')
        folha = FolhaDePagamento(valorHora, quantidadeHora, valorDesconto)
        folha.calcularSalarioBruto()
        folha.aplicarDescontoFolhaPagamento()
        print(f"Salário Bruto:  {folha.salarioBruto}")
        print(f"Salário Líquido:  {folha.salarioLiquido}")
    except Exception as err:
        print(f"\nValor digitado incorreto! {err}")
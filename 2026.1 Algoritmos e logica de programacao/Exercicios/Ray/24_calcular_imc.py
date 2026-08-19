import os


class CalcularIMC:
    imc: float
    categoriaIMC: str
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        
    def calcularIMC(self):
        self.imc = self.peso / (self.altura * self.altura)
            
    def verificarGrupoIMC(self):
        if self.imc < 18.5:
            self.categoriaIMC = "Abaixo do Peso"
        elif self.imc < 24.9:
            self.categoriaIMC = "Peso Normal"
        elif self.imc < 29.9:
            self.categoriaIMC = "Sobrepeso"
        elif self.imc < 34.9:
            self.categoriaIMC = "Obesidade I"
        elif self.imc < 40:
            self.categoriaIMC = "Obesidade II"
        else:
            self.categoriaIMC = "Obesidade III"
        
    def __repr__(self):
        return self.categoriaIMC

if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de cálculo de IMC!\n")
        altura = float(input("Digite a sua altura:\n"))
        peso = float(input("Digite o seu peso:\n"))
        os.system('cls')
        imc = CalcularIMC(peso, altura)
        imc.calcularIMC()
        imc.verificarGrupoIMC()
        print(imc)
    except Exception as err:
        print(f"\nValor digitado incorreto!")
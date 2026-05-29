import os


class AreaRetangular:
    area: float
    def __init__(self, largura, altura):
        self.larguraX = largura
        self.alturaY = altura
        
    
    def calcularArea(self):
        self.area = self.larguraX * self.alturaY
    
    def __repr__(self):
        return f"O cálculo de área das medidas em largura: {self.larguraX:.2f} e altura:{self.alturaY:.2f} calculadas equivalem a {self.area:.2f}² de área!!"

if __name__ == "__main__":
    try:
        os.system("cls")
        print("Bem-vindo ao sistema de cáluclo de retangulos!!\n")
        largura = float(input("Digite a largura do corpo!\n"))
        altura = float(input("Digite a altura do corpo!\n"))
        os.system("cls")
        areaR = AreaRetangular(largura, altura)
        area = areaR.calcularArea()
        print(areaR)
        
    except Exception as err:
        print(f"\nValor digitado incorreto! {err}")
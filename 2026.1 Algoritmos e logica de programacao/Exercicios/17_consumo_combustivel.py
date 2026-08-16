import os


class ConsumoMedio:
    consumoMedio: float
    def __init__(self, distanciaPercorrida, combustivelUtilizado):
        self.distanciaPercorrida = distanciaPercorrida
        self.combustivelUtilizado = combustivelUtilizado
    
    def calcularComsumoMedio(self):
        self.consumoMedio = self.distanciaPercorrida / self.combustivelUtilizado
    
if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de cálculo do consumo médio de combustível!\n")
        distanciaPercorrida = float(input("Digite a distância percorrida:\n"))
        combustivelUtilizado = float(input("Digite a quantidade de combustível utilizado na distância:\n"))
        os.system('cls')
        consumoMedio = ConsumoMedio(distanciaPercorrida, combustivelUtilizado)
        consumoMedio.calcularComsumoMedio()
        print(f"\n\n\n\nConsumo Médio de combustível em litros:  {consumoMedio.consumoMedio:.2f}\n\n\n\n\n")
    except Exception as err:
        print(f"\nValor digitado incorreto!")
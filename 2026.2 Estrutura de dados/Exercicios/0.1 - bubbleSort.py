class Vetores:
    matriz = []
    
    def __init__(self, matriz):
        self.matriz = matriz
    
    def mostrarVetores(self):
        texto = ''
        for i in range(len(self.matriz)):
            if i != len(self.matriz) - 1:
                texto = texto + f'| {self.matriz[i]} '
            elif i == len(self.matriz) - 1:
                texto = texto + f'| {self.matriz[i]} |'
        print(texto)
            
    def ordenarVetores(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                a1 = self.matriz[i]
                a2 = self.matriz[j]
                if a1 < a2:
                    self.matriz[i] = a2
                    self.matriz[j] = a1
                
            
if __name__ == '__main__':
    vetores = Vetores([10, 9, 8, 7, 6, 5, 2, 3, 1, 4])
    vetores.mostrarVetores()
    vetores.ordenarVetores()
    vetores.mostrarVetores()
    

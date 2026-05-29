import os

class VerificarVelocidade:
    ehInfracao: bool
    def __init__(self, velocidade):
        self.velocidade = velocidade
    
    def verificarSeInfracao(self):
        if self.velocidade > 80:
            self.ehInfracao = True
        else:
            self.ehInfracao = False
        
    def __repr__(self):
        return "Você foi multado" if self.ehInfracao else "Velocidade permitida"
    
if __name__ == "__main__":
    try:
        os.system('cls')
        print("Bem-vindo ao sistema de verificar velocidade!\n")
        velocidade = int(input("Digite a velocidade(km/h):\n"))
        os.system('cls')
        velocidade = VerificarVelocidade(velocidade)
        velocidade.verificarSeInfracao()
        print(velocidade)
    except Exception as err:
        print(f"\nValor digitado incorreto! {err}")
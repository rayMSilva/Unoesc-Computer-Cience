
import os


class ConversaoCelsiusParaFahrenheit:
    celcius: float 
    fahrenheit: float
    def __init__(self, celcius: float):
        self.celcius = celcius
        
    def converter(self):
        self.fahrenheit = (self.celcius * 9/5) + 32
        
    def __repr__(self):
        return f"A temperatura convertida em Celcius {self.celcius:.2f}C° para Fahrenheit é: {self.fahrenheit:.2f}F°"
    
    
    
if __name__ == "__main__":
    try:
        os.system("cls")
        print("Bem-vindo ao sistema de conversão de temperatura!\n")
        celcius = float(input("Digite a temperatura em celcius desejada:\n"))
        os.system("cls")
        conversao = ConversaoCelsiusParaFahrenheit(celcius)
        conversao.converter()
        print(conversao)
    except Exception as err:
        print("\nValor digitado incorreto!")

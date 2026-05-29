def subtracao():
    try:
        num1 = int(input("Digite o 1° número da subtração:\n"))
        num2 = int(input("Digite o 2° número da subtração:\n"))
        
        subtracao = num1 - num2
        
        print(f"A subtração do número {num1} e {num2} é: {subtracao}")
    except Exception as e:
        print("Erro de execução")
        
if __name__ == "__main__":
    subtracao()
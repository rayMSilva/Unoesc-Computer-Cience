def adicao():
    try:
        num1 = int(input(f"Digite o 1° número da adição:\n"))
        num2 = int(input(f"Digite o 2° número da adição:\n"))
        
        soma = num1 + num2
        
        print(f"A soma de {num1} e {num2} é: {soma}")
    except Exception as e:
        print("Erro de execução.")

if __name__ == "__main__":
    adicao()
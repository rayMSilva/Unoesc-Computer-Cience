from asyncio import sleep
import os


if __name__ == "__main__":
    try:
        senha = "1234"
        senhaDigitada = None
        print("Sistema de login com infinitas tentativas")
        while senhaDigitada != senha:
            senhaDigitada = None
            senhaDigitada = input("Digite a senha para entrar no app:\nou Ctrl+C para sair\n")
            if(senhaDigitada != senha):
                print("Senha incorreta! :(\n")
        if senhaDigitada == senha:
            print("Login realizado com sucesso!")
    except Exception as e:
        print("error")
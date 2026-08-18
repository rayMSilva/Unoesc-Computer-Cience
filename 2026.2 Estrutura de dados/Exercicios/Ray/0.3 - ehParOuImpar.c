#include <stdio.h>
#include <stdbool.h>
bool ehPar(int valor) {
    return valor % 2 == 0;
}

int main()
{
    printf("Bem vindo ao sistema de definição de pares ou impares\n");
    while(1) {
        int numero;
        printf("Digite o valor inteiro e eu definirei se o valor é par ou impar ou CTRL + C para SAIR!!\n");
        scanf("%d", &numero);
        if (ehPar(numero)) {
            printf("O valor digitado é par\n");
        }
        else if (!ehPar(numero)) {
            printf("O valor digitado é ímpar\n");
        }
    }
    
}
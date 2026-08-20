#include <stdio.h>

double calcularProgressao(int n) {
        double soma = 0;
        for(int i=1; i<n+1; i++) {
            soma += 1.0/i;
        }
        return soma;
}


int main()
{
    int valor = 0;
    while (1) {
        printf("Digite um valor inteiro e eu irei calcular sua progressao ou CTRL + C para SAIR!!\n");
        if (scanf("%d", &valor) == 1 && valor > 0) {
            double resultado = calcularProgressao(valor);
            printf("O valor final é %.2f\n\n", resultado);
        } else {
            printf("O valor deve ser um digito inteiro e maior que zero!\n\n");
            while (getchar() != '\n');
        }
    }
}
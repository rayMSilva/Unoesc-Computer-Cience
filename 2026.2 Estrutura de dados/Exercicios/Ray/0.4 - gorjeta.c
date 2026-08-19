#include <stdio.h>
void calcularGorjeta(double valor, double taxa) {
    if (valor > 0) {
        double taxaDeGarcom = valor * (taxa / 100);
        printf("\n\n******Conta restaurante******");
        printf("consumo restaurante: %.2f\n", valor);
        printf("taxa: %.2f\n", taxaDeGarcom);
        printf("total: %.2f\n\n", taxaDeGarcom + valor);
    } else {
    printf("O valor informado deve ser maior que zero\n\n");
    }
}

int main() {
    printf("Bem vindo ao sistema de definição de gorjeta\n");
    while(1) {
        double valor;
        printf("Digite o valor de consumo no restaurante ou aperte CTRL + C para SAIR!!!\n");
        scanf("%lf", &valor);
        calcularGorjeta(valor, 5);
    }   
}
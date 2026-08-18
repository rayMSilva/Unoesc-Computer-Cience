#include <stdio.h>
double dolarParaReais(double dolar, double cotacao){
    double reais = dolar * cotacao;
    return reais;
}

double reaisParaDolar(double reais, double cotacao){
    double dolares = reais / cotacao;
    return dolares;
}

int main()
{
    while(1){
        double numero;
        int funcao;
        printf("Digite o valor do seu saldo bancário\n");
        scanf("%lf", &numero);
        printf("Escolha uma conversão (1)U$ => R$ e (2)R$ => U$ \n");
        scanf("%d", &funcao);
        if (funcao == 1){
            double valor = dolarParaReais(numero, 5.20);
            printf("O valor da conversão é %.2f \n", valor);
        }else if(funcao == 2){
            double valor = reaisParaDolar(numero, 5.20);
            printf("O valor da conversão é %.2f \n", valor);
        }else{
            printf("pateta \n");
        }}
    
}
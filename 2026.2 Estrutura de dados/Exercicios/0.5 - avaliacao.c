#include <stdio.h>

void cadastrarVetor(int vetor[], int elementos) {
    for(int i = 0; i < elementos; i++) {
        while(1) {
            printf("Digite o valor do elemento na posição V[%d]\n", i);
            if(scanf("%d", &vetor[i]) == 1) {
                break;
            } else {
                printf("valor digitado precisa ser um inteiro! Digite novamente\n\n");
                while (getchar() != '\n');
            }
        }
    }
}

 void mostrarVetor(int vetor[], int elementos) {
    for(int i = 0; i < elementos; i++){
        if (i != elementos -1) {
            printf("Posição V[%d]: valor %d\n", i, vetor[i]);
        } else {
            printf("Posição V[%d]: valor %d\n\n", i, vetor[i]);
        }
    }
}

int alterarVetor(int vetor[], int elementos, int procurado, int novoValor) {
    int elementosAlterados = 0;
    for(int i = 0; i<elementos; i++) {
        if(vetor[i] == procurado) {
            vetor[i] = novoValor;
            elementosAlterados++;
        }
    }
    return elementosAlterados;
}

int main() {
    int vetor[10];
    printf("Bem vindo ao sistema de gerenciamento de vetores!\n");
    printf("Para sair do sistema use CTRL + C!!\n\n");
    cadastrarVetor(vetor, 10);
    mostrarVetor(vetor, 10);
    alterarVetor(vetor,10, 1, 2);
    mostrarVetor(vetor, 10);
}
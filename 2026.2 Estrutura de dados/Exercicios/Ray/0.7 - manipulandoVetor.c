#include <stdio.h>

void cadastrarVetor(int vetor[], int qtdElementos) {
    for (int i = 0; i < qtdElementos; i++) {
        while (1) {
            printf("Digite o valor inteiro da posicao V[%d]:\n", i);
            if (scanf("%d", &vetor[i]) == 1) {
                break;
            } else {
                printf("valor digitado precisa ser um inteiro! Digite novamente\n\n");
                while (getchar() != '\n');
            }
        }
    }
}

int somarVetor(int vetor[], int qtdElementos) {
    int soma = 0;
    for (int i = 0; i < qtdElementos; i++) {
        soma += vetor[i];
    }
    return soma;
}

int buscar(int vetor[], int qtdElementos, int pesquisa) {
    for (int i = 0; i < qtdElementos; i++) {
        if (pesquisa == vetor[i]) {
            return i;
        }
    }
    return -1;
}

void inverter(int vetor[], int qtdElementos) {
    for (int i = 0; i < qtdElementos; i++) {
        for (int j = 0; j < qtdElementos; j++) {
            if (i + j == qtdElementos - 1 && i < j) {
                int a1 = vetor[i];
                int a2 = vetor[j];
                vetor[i] = a2;
                vetor[j] = a1;
            }
        }
    }
}

void bbSort(int vetor[], int qtdElementos) {
    for (int i = 0; i < qtdElementos; i++) {
        for (int j = 0; j < qtdElementos; j++) {
            int a1 = vetor[i];
            int a2 = vetor[j];
            if (a1 < a2) {
                vetor[i] = a2;
                vetor[j] = a1;
            }
        }
    }
}

void maiorEPosicao(int vetor[], int qtdElementos, int *maior, int *posicao) {
    *maior = vetor[0];
    *posicao = 0;
    for (int i = 0; i < qtdElementos; i++) {
        if (vetor[i] > *maior) {
            *maior = vetor[i];
            *posicao = i;
        }
    }
}

void mostrarVetor(int vetor[], int elementos) {
    for (int i = 0; i < elementos; i++) {
        if (i != elementos - 1) {
            printf("posicao V[%d]: valor %d\n", i, vetor[i]);
        } else {
            printf("posicao V[%d]: valor %d\n\n", i, vetor[i]);
        }
    }
}

int main() {
    int TAM = 10;

    int vetor[10] = {0};

    printf("Bem vindo ao sistema de gerenciamento de vetores!\n");
    printf("Para sair do sistema use CTRL + C!!\n\n");

    cadastrarVetor(vetor, TAM);

    bbSort(vetor, TAM);
    inverter(vetor, TAM);
    mostrarVetor(vetor, TAM);

    int soma = somarVetor(vetor, TAM);
    printf("A soma de todos os valores do vetor cadastrado eh %d\n\n", soma);

    printf("Buscando valor 9\n\n");
    if (buscar(vetor, TAM, 9) != -1) {
        printf("Valor 9 encontrado no vetor\n");
    } else {
        printf("Valor 9 nao encontrado no vetor\n\n");
    }

    printf("Invertendo vetor\n\n");
    inverter(vetor, TAM);
    mostrarVetor(vetor, TAM);

    printf("Buscando maior valor\n\n");
    int maior, posicao;
    maiorEPosicao(vetor, TAM, &maior, &posicao);
    printf("o maior valor eh %d e sua posicao eh %d\n\n", maior, posicao);

    return 0;
}
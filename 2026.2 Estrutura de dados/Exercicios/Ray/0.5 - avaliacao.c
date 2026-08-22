#include <stdio.h>

int lerInteiro(char *mensagem) {
    int valor;
    while (1) {
        printf("%s", mensagem);
        if (scanf("%d", &valor) == 1) {
            break;
        } else {
            printf("Valor inválido! Digite um número inteiro.\n\n");
            while (getchar() != '\n');
        }
    }
    return valor;
}   

void cadastrarVetor(int vetor[], int elementos) {
    for (int i = 0; i < elementos; i++) {
        char mensagem[100];
        sprintf(mensagem, "Digite o valor do elemento na posição V[%d]\n", i);
        vetor[i] = lerInteiro(mensagem);  
    }
}

void mostrarVetor(int vetor[], int elementos) {
    for (int i = 0; i < elementos; i++) {
        if (i != elementos - 1) {
            printf("Posição V[%d]: valor %d\n", i, vetor[i]);
        } else {
            printf("Posição V[%d]: valor %d\n\n", i, vetor[i]);
        }
    }
}

int alterarVetor(int vetor[], int elementos, int procurado, int novoValor) {
    int elementosAlterados = 0;
    for (int i = 0; i < elementos; i++) {
        if (vetor[i] == procurado) {
            vetor[i] = novoValor;
            elementosAlterados++;
        }
    }
    return elementosAlterados;
}

void exibirAcoes() {
    printf("Operações disponíveis para realizar com seu vetor ou CTRL + C para SAIR!!\n");
    printf("1 - Alterar Vetor\n");
    printf("2 - Mostrar Vetor\n\n");
}


int main() {
    int tam = 10;
    int vetor[10];

    printf("Bem vindo ao sistema de gerenciamento de vetores!\n");
    printf("Para sair do sistema use CTRL + C!!\n\n");

    cadastrarVetor(vetor, tam);
    mostrarVetor(vetor, tam);

    while (1) {
        exibirAcoes();
        int acao = lerInteiro("Digite a ação desejada:\n");

        if (acao == 1) {
            int valorProcurado = lerInteiro("Digite um valor inteiro que deseja procurar no vetor cadastrado!\n");
            int novoValor = lerInteiro("Digite um valor inteiro que deseja substituir o valor procurado no vetor cadastrado!\n");

            int totalAlterado = alterarVetor(vetor, tam, valorProcurado, novoValor);
            if (totalAlterado > 0) {
                printf("Elementos alterados com sucesso, foram alteradas %d posições!\n\n", totalAlterado);
            } else {
                printf("O valor não foi encontrado. Nenhuma posição foi alterada!\n\n");
            }
        } else if (acao == 2) {
            mostrarVetor(vetor, tam);
        } else {
            printf("Valor inserido não é uma operação válida!!\n\n");
        }
    }
}
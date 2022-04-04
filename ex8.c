// Exercicio 8 - L6 (Lista duplamente encadeada com ordenação por bubble sort)
// 04.04.2022

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct aluno
{
    int dia;
    int mes;
    int ano;
    int matricula;
    char *nome;
    struct aluno *proximo;
    struct aluno *anterior;
} aluno;

aluno *cria_turma(aluno *matriculado);
void insere_turma(aluno **matriculado);
void ordena_alunos(aluno **matriculado);

int main(void)
{
    int i, n;
    scanf("%d", &n);
    if (!n || n > 30)
        return 0;
    aluno *matriculado = cria_turma(matriculado);
    for (i = 0; i < n; i++)
        insere_turma(&matriculado);
    ordena_alunos(&matriculado);
    while (matriculado->proximo)
    {
        printf("Matric.: %d Nome: %s Data Nasc: %d/%d/%d\n", matriculado->matricula, matriculado->nome, matriculado->dia, matriculado->mes, matriculado->ano);
        matriculado = matriculado->proximo;
    }
    free(matriculado);
    return 0;
}

aluno *cria_turma(aluno *matriculado)
{
    aluno *aux;
    aux = malloc(sizeof(*aux));
    if (!aux)
        return NULL;
    aux->anterior = NULL;
    aux->proximo = NULL;
    return aux;
}

void insere_turma(aluno **matriculado)
{
    int i;
    aluno *aux = *matriculado;
    aluno *futuro_aluno;
    while (aux->proximo)
        aux = aux->proximo;
    aux->nome = malloc(sizeof(char) * 200);
    if (!aux->nome)
        return;
    scanf("%d %d %d %d %200[^\n]", &aux->matricula, &aux->dia, &aux->mes, &aux->ano, aux->nome);
    scanf("%*c");
    futuro_aluno = malloc(sizeof(*futuro_aluno));
    if (!futuro_aluno)
        return;
    futuro_aluno->proximo = NULL;
    futuro_aluno->anterior = aux;
    aux->proximo = futuro_aluno;
}

void ordena_alunos(aluno **matriculado)
{
    int i, j;
    aluno *aux = *matriculado;
    aluno *ant, *post;
    while (aux->proximo->proximo)
    {
        if (aux->ano < aux->proximo->ano)
        {
            if (aux->anterior)
                aux->anterior->proximo = aux->proximo;
            aux->proximo->proximo->anterior = aux; // 3 olha para trás em 1
            post = aux->proximo; // Guarda o 2
            aux->proximo = aux->proximo->proximo; // 1 olha para frente em 3
            ant = aux->anterior; // Guarda o anterior a 1
            aux->anterior = post; // 1 olha para trás em 2
            post->anterior = ant; // 2 olha para trás em L-86
            post->proximo = aux; // 2 olha para frente em 1
            aux = aux->proximo; // Avanca o 
            continue;
        }
        if (aux->ano == aux->proximo->ano)
        {
            if (aux->mes == aux->proximo->mes)
            {
                if (aux->dia < aux->proximo->dia)
                {
                    if (aux->anterior)
                        aux->anterior->proximo = aux->proximo;
                    aux->proximo->proximo->anterior = aux;
                    post = aux->proximo;
                    aux->proximo = aux->proximo->proximo;
                    ant = aux->anterior;
                    aux->anterior = aux->proximo;
                    post->anterior = ant;
                    post->proximo = aux;
                    aux = aux->proximo;
                    continue;
                }
            }
            if (aux->mes < aux->proximo->mes)
            {
                if (aux->anterior)
                    aux->anterior->proximo = aux->proximo;
                aux->proximo->proximo->anterior = aux;
                post = aux->proximo;
                aux->proximo = aux->proximo->proximo;
                ant = aux->anterior;
                aux->anterior = aux->proximo;
                post->anterior = ant;
                post->proximo = aux;
                aux = aux->proximo;
                continue;
            }
        }
    }
    while (aux->anterior) // Volta ao primeiro endereco
        aux = aux->anterior;
    *matriculado = aux;
}

// Vitor Lima Ribeiro - github.com/TheLastAurora //
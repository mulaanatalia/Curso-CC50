#include <stdio.h>
#include <cs50.h> //Adicionar a biblioteca do CS50

int main(void)
{
    int n;

    do{

    n = get_int("Insira o tamanho da pirâmide: ");

    }

    while(n < 1);

     if (n > 0 && n < 9){

        for(int i = 1; i <= n; i++){

            for(int j = 1; j <= i; j++)
                printf("#");
               printf("\n");

    }

 }
}
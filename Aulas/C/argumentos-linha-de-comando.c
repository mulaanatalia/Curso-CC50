#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    //IMPRIME O NOME QUE PASSAMOS COMO PARAMENTRO DO METODO MAIN
    /*if (argc == 2)
    {
        printf("oi, %s\n", argv[1]);
    }
    else
    {
        printf("olá, mundo\n");
    }*/

    //IMPRIME CADA CARACTERE INDIVIDUALMENTE
    if (argc == 2)
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            printf("%c\n", argv[1][i]);
        }
    }
}
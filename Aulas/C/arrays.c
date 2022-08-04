#include <stdio.h>
#include <cs50.h>

const int TOTAL = 3;
//Prototipo
float media(int length, int array[]);

int main(void)
{
    //int total = get_int("Total de números: ";)
    int scores[TOTAL];
    for (int i = 0; i < TOTAL; i++)
    {
        scores[i] = get_int("Pontuação: ");
    }
    printf("Média:%f\n", media(TOTAL, scores));
}

float media(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum = sum + array[i];
    }
    return sum / (float) length;
}
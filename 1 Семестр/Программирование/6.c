#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <string.h>

int main()
{
    char array[5] = "Hello";
    char *a_array;
    a_array = array;

    for (int i = 0; i < 5; i++)
        printf("%c", a_array[i]);
    printf("\n\n");

    char *str;
    str = (char *) malloc(5);
    strcpy(str, "Hello");
    for (int i = 0; i < 5; i++)
        printf("%c", str[i]);
    printf("\n");
    free(str);
}
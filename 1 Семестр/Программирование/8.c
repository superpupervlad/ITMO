#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    //1 Task
    char *string1 = (char *)malloc(sizeof(char) * 32);
    char *string2 = (char *)malloc(sizeof(char) * 32);
    scanf("%s%s", string1, string2);
    char *string_final = (char *)malloc(sizeof(char) * 64);
    strcat(string_final, string1);
    strcat(string_final, string2);
    printf("%s\n", string_final);
    //2 Task
    int n;
    scanf("%d", &n);
    if (strncmp(string1, string2, n) == 0)
        printf("Первые %d символов в строках идентичны\n", n);
    else
        printf("Первые %d символов в строках не идентичны\n", n);
    //3 Task
    printf("Длина строки:%lu\n", strlen(string_final));
    //4 Task
    char *istr;
    istr = strstr (string1,string2);
    printf("Строка начинается с %lu символа\n", istr-string1+1);
    //5 Task
    printf("Длина отрезка:%lu\n", strlen(strstr(string1, &string2[0])));
}
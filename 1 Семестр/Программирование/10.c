#include <stdio.h>
#include <string.h>
#include <malloc.h>

int sum(int a)
{
    if (a == 0)
        return 0;
    return (a % 10) + sum(a / 10);
}

void s(char *str, int pos) {
    int i;
    if ((str[pos] == ' ') && (str[pos + 1]) == ' ')
        s(str, pos + 1);
    for (i = pos; i < strlen(str) - 1; i++)
        str[i] = str[i + 1];
    str[i] = 0;
}

int main (void){
    int a, i;
    char str[100];
	fgets(str, 100, stdin);
    for (i = 0; i < strlen(str); i++)
        if ((str[i] == ' ') && (str[i + 1] == ' '))
            s(str, i + 1);
    for (i = 0; i < strlen(str); i++)
        if (((str[i] == '{') || (str[i] == '(') || (str[i] == '[') || (str[i] == '"')  || (str[i] == ',')) && (str[i + 1] == ' '))
            s(str, i + 1);
    printf("%s\n", str);
    scanf("%d", &a);
    printf("%d\n", sum(a));
    return 0;
}

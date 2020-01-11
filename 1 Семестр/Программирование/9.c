#include <stdio.h>

void primes (void){
    int end, i, j;
    scanf("%d", &end);
    int check = 0;
    for (i = 2; i <= end; i++){
        for (j = 2; j <= i/2; j++)
            if (i % j == 0){
                check = 1;
                break;
            }
        if (check == 0)
            printf("%d\n", i);
    check = 0;
    }
}

void bank (void){
    int i, months;
    float money, interest_rate, in_bank;
    scanf("%f\n%d\n%f", &money, &months, &interest_rate);
    for (i = 0; i < months; i++){
        money = money + ((float)1/12 * interest_rate);
        printf("%.3f\n", money);
    }
}

int main (void){
    primes();
    bank();
}
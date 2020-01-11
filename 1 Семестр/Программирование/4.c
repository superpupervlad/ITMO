#include <stdio.h>

void not_if(a){
    while (a >= 65){
	    while (a <= 87){
	        printf("In range\n");
	        return;
	    }
	    printf("Not in range\n");
	    return;
	}
	printf("Not in range\n");
}

int main(void) {
	int a;
	scanf("%d", &a);
	not_if(a);
	scanf("%d", &a);
    printf("%d", (a >> 23) % 2);

	return 0;
}
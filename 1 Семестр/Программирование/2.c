#include <stdio.h>
#include <math.h>

int main(void) {
	float a;
	scanf("%f", &a);
	float result1 = (sin(2*a)+sin(5*a)-sin(3*a))/(cos(a)-cos(3*a)+cos(5*a));
	float result2 = tan(3*a);
	printf("%f\n%f", result1, result2);
	return 0;
}
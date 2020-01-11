#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	char* file = argv[1];
	FILE *f;
	f = freopen(file, "w", stdout);
	char *p;
	int a,b,c;
	a = strtol(argv[2], &p, 10);
	b = strtol(argv[3], &p, 10);
	c = a + b;
	printf("%d\n",c);
	fclose(f);
	return 0;
}

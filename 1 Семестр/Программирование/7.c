#include <stdio.h>
#include <math.h>
#include <stdlib.h>

enum car {TRUCK,VAN,SPORTCAR,SEDAN,PICKUP,BUS};

struct rect {float x1, x2, x3, x4, y1, y2, y3, y4, a, b, c, P;};

union
{
    unsigned a;
    struct b
    {
        unsigned play: 1;
        unsigned pause: 1;
        unsigned record: 1;
    }b;
}c;

int main(){
enum car x=BUS;
printf("%d\n",x);

struct rect abcd;
abcd.x1=0; abcd.x2=0; abcd.x3=1; abcd.x4=1; abcd.y1=0; abcd.y2=1; abcd.y3=0; abcd.y4=1;
abcd.a=sqrt(pow(abcd.x2-abcd.x1,2) + pow(abcd.y2-abcd.y1,2));
abcd.b=sqrt(pow(abcd.x4-abcd.x3,2) + pow(abcd.y4-abcd.y3,2));
abcd.P=abcd.a*2 + abcd.b*2;
printf("%.2f\n",abcd.P);

scanf("%x", &c.a);
printf("%d %d %d\n", c.b.play, c.b.pause, c.b.record);
}

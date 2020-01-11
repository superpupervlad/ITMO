#include <stdio.h>
#include "par.c"
 
int main() {
    struct par new_par;
    scanf("%f %f %f %f %f %f %f %f",
    &new_par.x1, &new_par.y1, &new_par.x2,
    &new_par.y2, &new_par.x3, &new_par.y3,
    &new_par.x4, &new_par.y4);
    printf("P: %f\n", p_par(new_par));
    printf("S: %f\n", s_par(new_par));
    return 0;
}
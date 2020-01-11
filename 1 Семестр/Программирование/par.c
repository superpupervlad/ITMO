#include <math.h>
#include "par.h"
 
float p_par(struct par new_par){
    float ab, ac, cd, bd;
    ab = sqrt(((pow((new_par.x2 - new_par.x1),2)) + pow((new_par.y2 - new_par.y1),2)));
    ac = sqrt(((pow((new_par.x3 - new_par.x1),2)) + pow((new_par.y3 - new_par.y1),2)));
    cd = sqrt(((pow((new_par.x3 - new_par.x4),2)) + pow((new_par.y3 - new_par.y4),2)));
    bd = sqrt(((pow((new_par.x2 - new_par.x4),2)) + pow((new_par.y2 - new_par.y4),2)));
    float p = ab + ac + cd + bd;
    return p;
}
 
float s_par(struct par new_par){
    float a, b, cosfi, sinfi, s;
    a = sqrt(pow((new_par.x3 - new_par.x2), 2) + pow((new_par.y3 - new_par.y2), 2));
    b = sqrt(pow((new_par.x3 - new_par.x4), 2) + pow((new_par.y3 - new_par.y4), 2));
    cosfi = ((new_par.x2 - new_par.x3)*(new_par.x3 - new_par.x4) + (new_par.y2 - new_par.y3)*(new_par.y3 - new_par.y4))/(a*b);
    sinfi = sqrt(1 - pow(cosfi, 2));
    s = a*b*sinfi;
    return s;
}
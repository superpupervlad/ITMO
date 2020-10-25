#include "functions.h"

void change_biggest(int& a, int& b){
    if (a > b)
        a = a % b;
    else
        b = b % a;
}

void change_biggest(int* a, int* b){
    if (*a > *b)
        *a = *a % *b;
    else
        *b = *b % *a;
}

void inverse(double& a){
    a = 1/a;
}

void inverse(double* a){
    *a = 1/ *a;
}

void decrease(circle& circle, double& a){
    circle.r = circle.r - a;
}

void decrease(circle* circle, double* a){
    circle->r = (*circle).r - *a;
}

void change_lines(matrix& matrix, int& line1, int& line2){
    int temp;
    for (int i = 0; i < 3; i++){
        temp = matrix.elements[line1][i];
        matrix.elements[line1][i] = matrix.elements[line2][i];
        matrix.elements[line2][i] = temp;
    }
}

void change_lines(matrix* matrix, int* line1, int* line2){
    int temp;
    for (int i = 0; i < 3; i++){
        temp = matrix->elements[*line1][i];
        matrix->elements[*line1][i] = matrix->elements[*line2][i];
        matrix->elements[*line2][i] = temp;
    }
}

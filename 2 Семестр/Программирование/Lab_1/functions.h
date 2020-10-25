#ifndef functions_h
#define functions_h

// Task 3
void change_biggest(int& , int&);
void change_biggest(int* , int*);

// Task 8
void inverse(double&);
void inverse(double*);

// Task 11
struct circle{
    double x, y, r;
};
void decrease(circle&, double&);
void decrease(circle*, double*);

// Task 16
struct matrix{
    int elements[3][3];
};
void change_lines(matrix&, int&, int&);
void change_lines(matrix*, int*, int*);
#endif

#include "Kubik.h"
#include <iostream>

using std::cout;
using std::cin;

Side::Side(char c)
{   
    main_color = c;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
        data[i][j] = main_color;
}

Kubik::Kubik()
{
    correct = true;
}

void Side::p()
{
    cout << '\n';
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++)
            cout << data[i][j];
        cout << '\n';
    }
    cout << '\n';
}

void Kubik::print()
{
    cout << '\n' << 'F';
    F.p();
    cout << 'U';
    U.p();
    cout << 'B';
    B.p();
    cout << 'D';
    D.p();
    cout << 'R';
    R.p();
    cout << 'L';
    L.p();
}

/* Number of rows for cpy function
 *   3  4  5
 * 0 .  .  .
 * 1 .  .  .
 * 2 .  .  .
 */

void cpy(int row, char a[][3], char b[]){ // for temp
    if (row < 3)
        for(int i = 0; i < 3; i++)
            a[row][i] = b[i];
    else
        for(int i = 0; i < 3; i++)
            a[i][row % 3] = b[i];
}

void cpy(int row, char a[], char b[][3]){ // for temp
    if (row < 3)
        for(int i = 0; i < 3; i++)
            a[i] = b[row][i];
    else
        for(int i = 0; i < 3; i++)
            a[i] = b[i][row % 3];
}


void cpy(int row1, int row2, char a[][3], char b[][3]){ // a <- b
    if (row1 < 3)
        if (row2 < 3)
            for(int i = 0; i < 3; i++)
                a[row1][i] = b[row2][i];
        else
            for(int i = 0; i < 3; i++)
                a[row1][i] = b[i][row2 % 3];
    else
        if (row2 < 3)
            for(int i = 0; i < 3; i++)
                a[i][row1 % 3] = b[row2][i];
        else
            for(int i = 0; i < 3; i++)
                a[i][row1 % 3] = b[i][row2 % 3];
}

void Kubik::frotate(bool clockwise, bool check)
{   
    char temp[3];
    if (check == 1 and clockwise == 1)
        operations.push_back('f');
    if (clockwise){
        cpy(5, temp, L.data);
        cpy(5, 0, L.data, D.data);
        cpy(0, 3, D.data, R.data);
        cpy(3, 2, R.data, U.data);
        cpy(2, U.data, temp);
        
    }
    else{
        if (check)
            operations.push_back('F');
        for (int i = 0; i < 3; i++)
            frotate(1, 0);
    }
}

void Kubik::brotate(bool clockwise, bool check)
{
    char temp[3];
    if (check == 1 and clockwise == 1)
        operations.push_back('b');
    if (clockwise){
        cpy(5, temp, R.data);
        cpy(5, 2, R.data, D.data);
        cpy(2, 3, D.data, L.data);
        cpy(3, 0, L.data, U.data);
        cpy(0, U.data, temp);
    }
    else{
        if (check)
            operations.push_back('B');
        for (int i = 0; i < 3; i++)
            brotate(1, 0);
    }
}

void Kubik::lrotate(bool clockwise, bool check)
{
    char temp[3];
    if (check == 1 and clockwise == 1)
        operations.push_back('l');
    if (clockwise){
        cpy(5, temp, B.data);
        cpy(5, 3, B.data, D.data);
        cpy(3, 3, D.data, F.data);
        cpy(3, 3, F.data, U.data);
        cpy(3, U.data, temp);
    }
    else{
        if (check)
            operations.push_back('L');
        for (int i = 0; i < 3; i++)
            lrotate(1, 0);
    }
}

void Kubik::rrotate(bool clockwise, bool check)
{
    char temp[3];
    if (check == 1 and clockwise == 1)
        operations.push_back('r');
    if (clockwise){
        cpy(5, temp, D.data);
        cpy(5, 3, D.data, B.data);
        cpy(3, 5, B.data, U.data);
        cpy(5, 5, U.data, F.data);
        cpy(5, F.data, temp);
    }
    else{
        if (check)
            operations.push_back('R');
        for (int i = 0; i < 3; i++)
            rrotate(1, 0);
    }
}

void Kubik::urotate(bool clockwise, bool check)
{
    char temp[3];
    if (check == 1 and clockwise == 1)
        operations.push_back('u');
    if (clockwise){
        cpy(0, temp, L.data);
        cpy(0, 0, L.data, F.data);
        cpy(0, 0, F.data, R.data);
        cpy(0, 0, R.data, B.data);
        cpy(0, B.data, temp);
    }
    else{
        if (check)
            operations.push_back('U');
        for (int i = 0; i < 3; i++)
            urotate(1, 0);
    }
}

void Kubik::drotate(bool clockwise, bool check)
{
    char temp[3];
    if (check == 1 and clockwise == 1)
        operations.push_back('d');
    if (clockwise){
        cpy(2, temp, L.data);
        cpy(2, 2, L.data, B.data);
        cpy(2, 2, B.data, R.data);
        cpy(2, 2, R.data, F.data);
        cpy(2, F.data, temp);
    }
    else{
        if (check)
            operations.push_back('D');
        for (int i = 0; i < 3; i++)
            drotate(1, 0);
    }
}

void Kubik::randomize(int number_of_turns)
{
    for(int i = 0; i < number_of_turns; i++)
        switch(rand() % 6){
            case 0:
                frotate(rand() % 2);
                break;
            case 1:
                lrotate(rand() % 2);
                break;
            case 2:
                rrotate(rand() % 2);
                break;
            case 3:
                urotate(rand() % 2);
                break;
            case 4:
                drotate(rand() % 2);
                break;
            case 5:
                brotate(rand() % 2);
                break;
        }
}

bool Kubik::check()
{
    if (F.check() and U.check() and B.check() and D.check() and R.check() and L.check())
        correct = true;
    else
        correct = false;
    return correct;
}

bool Side::check()
{
    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            if (data[i][j] != data[1][1])
                return false;
    return true;
}

void Side::file_print(FILE *f)
{
    putc('\n', f);
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++)
            putc(data[i][j], f);
        putc('\n', f);
    }
}

void Kubik::file_print(FILE *f)
{
    fputc('F', f);
    F.file_print(f);
    fputc('U', f);
    U.file_print(f);
    fputc('B', f);
    B.file_print(f);
    fputc('D', f);
    D.file_print(f);
    fputc('R', f);
    R.file_print(f);
    fputc('L', f);
    L.file_print(f);
}

void Kubik::save()
{
    FILE *f;
    f = fopen("kubik.txt", "w");

    fprintf(f, "Operations: ");
    for(int i = 0; i < operations.size(); i++)
        putc(operations[i], f);
    fprintf(f, "\nCube condition:\n");
    file_print(f);
}

void Kubik::load()
{
    FILE *f;
    f = fopen("kubik.txt", "r");
    
    fseek(f, 12, SEEK_SET);
    operations.clear();
    char c;
    c = fgetc(f);
    while(c != '\n'){
        operations.push_back(c);
        c = fgetc(f);
    }
    fseek(f, 18, SEEK_CUR);
    
    for(int z = 0; z < 6; z++){
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++)
                sides[z]->data[i][j] = fgetc(f);
            fgetc(f);
        }
        fgetc(f); fgetc(f);
    }
}

void Kubik::solve()
{
    if(check())
        return;
    while(operations.size() > 0){
        switch(operations.back()){
            case 'f':
                frotate(0, 0);
                break;
            case 'F':
                frotate(1, 0);
                break;
            case 'u':
                urotate(0, 0);
                break;
            case 'U':
                urotate(1, 0);
                break;
            case 'b':
                brotate(0, 0);
                break;
            case 'B':
                brotate(1, 0);
                break;
            case 'd':
                drotate(0, 0);
                break;
            case 'D':
                drotate(1, 0);
                break;
            case 'r':
                rrotate(0, 0);
                break;
            case 'R':
                rrotate(1, 0);
                break;
            case 'l':
                lrotate(0, 0);
                break;
            case 'L':
                lrotate(1, 0);
                break;
        }
        operations.pop_back();
    }
}

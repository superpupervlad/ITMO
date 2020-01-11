#include <stdio.h>

int main(void){
    int a[9];
    //int a[9] = {12, 13, 14, 15, 16, 17, 18, 19, 20};
    scanf("%d%d%d%d%d%d%d%d%d", &a[0],&a[1],&a[2],&a[3],&a[4],&a[5],&a[6],&a[7],&a[8]);
    printf("a = [ ");
    for (int i = 0; i < sizeof(a)/sizeof(int); i++)
        printf("%d ", a[i]);
    printf("]\n");
    int m_1[2][2];
    m_1[0][0] = 2; m_1[0][1] = 1; m_1[1][0] = 1; m_1[1][1] = 3;
    int m_2[2][2];
    m_2[0][0] = 1; m_2[0][1] = 2; m_2[1][0] = 3; m_2[1][1] = 1;
    //m_2 = {{1,2},{3,1}};
    int result_matrix[2][2];
    for(int i = 0; i < 2; i++)
        for(int j = 0; j < 2; j++){
            result_matrix[i][j] = 0;
            for(int k = 0; k < 2; k++)
                result_matrix[i][j] += m_1[i][k] * m_2[k][j];
        }

    for(int i = 0; i < 2; i ++){
        for(int j = 0;j < 2;j++)
            printf("%d ",result_matrix[i][j]);
        printf("\n");
    }
}
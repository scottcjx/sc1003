#include <stdio.h>
#define SIZE 10
void reduceMatrix2D(int ar[][SIZE], int rowSize, int colSize); 
void display(int ar[][SIZE], int rowSize, int colSize);

int main()
{
    int ar[SIZE][SIZE], rowSize, colSize; int i,j;
    printf("Enter row size of the 2D array: \n"); scanf("%d", &rowSize);
    printf("Enter column size of the 2D array: \n"); scanf("%d", &colSize);
    printf("Enter the matrix (%dx%d): \n", rowSize, colSize); 
    for (i=0; i<rowSize; i++) for (j=0; j<colSize; j++) scanf("%d", &ar[i][j]);
    reduceMatrix2D(ar, rowSize, colSize); 
    printf("reduceMatrix2D(): \n"); 
    display(ar, rowSize, colSize);
    return 0;
}
void display(int ar[][SIZE], int rowSize, int colSize) {
    int l,m;
    for (l = 0; l < rowSize; l++)
    {
        for (m = 0; m < colSize; m++)
        {
            printf("%d ", ar[l][m]); printf("\n");
        }
    }
}

void reduceMatrix2D(int ar[][SIZE], int rowSize, int colSize)
{
    int col_sum;
    for (int j = 0; j < colSize; j++)
    {
        col_sum = 0;
        for (int i = 0; i < rowSize; i++)
        {
            // if curr row is less than or equal to curr col 
            // (left of diagonal)
            if (i >= j)
            {
                // add to sum of col
                col_sum += ar[i][j];
                // set value in place to 0
                ar[i][j] = 0;
            }
        }
        // set (x, x) value to sum of all values (x, x) and below
        ar[j][j] = col_sum;
    }

}

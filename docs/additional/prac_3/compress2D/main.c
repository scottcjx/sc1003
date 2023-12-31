#include <stdio.h>
#define SIZE 100
void compress2D(int data[SIZE][SIZE], int rowSize, int colSize);
int main()  
{
   int data[SIZE][SIZE];
   int i,j;
   int rowSize, colSize;
   printf("Enter the array size (rowSize, colSize): \n");
   scanf("%d %d", &rowSize, &colSize);  
   printf("Enter the matrix (%dx%d): \n", rowSize, colSize);
   for (i=0; i<rowSize; i++)
      for (j=0; j<colSize; j++)
         scanf("%d", &data[i][j]);      
   printf("compress2D(): \n");
   compress2D(data, rowSize, colSize);
   return 0;
}
void compress2D(int data[SIZE][SIZE], int rowSize, int colSize)  
{
   int prev_num = 0;
   int curr_count = 0;
   
   for (int i = 0; i < rowSize; i++)
   {
      curr_count = 1;
      prev_num = data[i][0];
       for (int j = 1; j < colSize + 1; j++)
       {
           if (j == colSize)
           {
               printf("%d %d\n", prev_num, curr_count);
           }
           else if (data[i][j] == prev_num)
           {
               curr_count++;
           }
           else
           {
               printf("%d %d ", prev_num, curr_count);
               curr_count = 1;
           }
           prev_num = data[i][j];
       }
   }
}
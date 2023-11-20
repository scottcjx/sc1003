# MatTriSum

[Read the Brief](./matTriSum.pdf)

## Contents
``` c
int matTriSum(int x[M][M], int n)
{
 int sum_m = 0;
 for (int i = 0; i < n; i++)
 {
     for (int j = 0; j < n; j++)
     {
         if (j >= i)
         {
             sum_m += x[i][j];
         }
     }
 }
 return sum_m;
}
```
# symmetry2D

``` c
int symmetry2D(int M[][SIZE], int rowSize, int colSize)  
{
    for (int i = 0; i < rowSize; i++)
    {
        for (int j = 0; j < colSize; j++)
        {
            if (M[i][j] != M[j][i]) return 0;
        }
    }
    return 1;
}
```
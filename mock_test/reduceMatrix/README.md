# Reduce Matrix

[Read the Brief](./reduceMatrix.pdf)

``` c
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
```
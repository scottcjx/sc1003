# minOfMax2D

``` c
int minOfMax2D(int ar[][SIZE], int rowSize, int colSize)
{
   int ar_smallestMax;
    int rowMax;

    for (int i = 0; i < rowSize; i++)
    {
        rowMax = 0;
        for (int j = 0; j < colSize; j++)
        {
            if (ar[i][j] > rowMax) rowMax = ar[i][j];
        }
        if (i == 0) ar_smallestMax = rowMax;
        else if (rowMax < ar_smallestMax) ar_smallestMax = rowMax;
    }

    return ar_smallestMax;
}
```
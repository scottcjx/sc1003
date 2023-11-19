# diagonals2D

``` c
void diagonals2D(int ar[][SIZE], int rowSize, int colSize, int *sum1, int *sum2)
{
    *sum1 = 0;
	*sum2 = 0;
	
	for (int i = 0; i < rowSize; i++)
	{
	    *sum1 += ar[i][i];
	    *sum2 += ar[i][(colSize-1)-i];
	}
}
```
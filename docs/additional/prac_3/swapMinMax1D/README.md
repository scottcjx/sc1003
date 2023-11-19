# swapMinMax1D
``` c
void swapMinMax1D(int ar[], int size)
{
    int idx_max = 0;
    int idx_min = 0;

    for (int i = 0; i < size; i++)
    {
        if (ar[i] >= ar[idx_max]) idx_max = i;
        if (ar[i] <= ar[idx_min]) idx_min = i;
    }

    int tmpval = ar[idx_min];
    ar[idx_min] = ar[idx_max];
    ar[idx_max] = tmpval;
}
```
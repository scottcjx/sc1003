#include <stdio.h>
void swapMinMax1D(int ar[], int size);
int main()  
{
   int ar[50],i,size;
    
   printf("Enter array size: \n");
   scanf("%d", &size);
   printf("Enter %d data: \n", size);
   for (i=0; i<size; i++)  
      scanf("%d",ar+i);
   swapMinMax1D(ar, size);
   printf("swapMinMax1D(): ");
   for (i=0; i<size; i++)  
      printf("%d ",*(ar+i));  
   return 0;
}

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
# Further Practice 6

## Contents

``` c
#include <stdio.h>
int main()
{
    int req_height;
    printf("Enter the height: \n");
    scanf(" %d", &req_height);

    printf("The pattern is: \n");
    for (int i = 1; i < req_height + 1; i++)
    {
        for (int j = 0; j < (req_height - i); j++)
        {
            printf("*");
        }
        for (int k = 0; k < i; k++)
        {
            printf("=");
        }
        printf("\n");
    }
 return 0;
} 
```
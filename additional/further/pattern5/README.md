# Further Practice 5

## Contents

``` c
#include <stdio.h>
int main()
{
    int req_height;
    printf("Enter the height: \n");
    scanf(" %d", &req_height);

    printf("The pattern is: \n");
    const char curr_char[] = {'+', '='};
    int char_count = 0;

    for (int i = 1; i < req_height+1; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf("%c", curr_char[(char_count % 2)]);
            char_count++;
        }
        for (int k = 0; k < (i-1); k++)
        {
            printf("%c", curr_char[(char_count % 2)]);
            char_count++;
        }
        
        printf("\n");
    }
    return 0;
} 
```

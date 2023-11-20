# pattern3

``` c
#include <stdio.h>
int main()
{
   int req_height;
   int add_val;
   printf("Enter the height: \n");
   scanf(" %d", &req_height);
   
   printf("The pattern is: \n");
   for (int i = 1; i < req_height + 1; i++)
   {
       for (int j = 0; j < i; j++)
       {
           add_val = (i+j);
           if (add_val > 9) add_val -= 10;
        printf("%d", add_val);
       }
       printf("\n");
   }
   return 0;
}
```
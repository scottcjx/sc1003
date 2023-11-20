#include <stdio.h>
#define INIT_VALUE 999
int extEvenDigits1(int num);
void extEvenDigits2(int num, int *result);
int main()
{
   int number, result = INIT_VALUE;
    
   printf("Enter a number: \n");
   scanf("%d", &number);
   printf("extEvenDigits1(): %d\n", extEvenDigits1(number));         
   extEvenDigits2(number, &result);
   printf("extEvenDigits2(): %d\n", result);
   return 0;
}
int extEvenDigits1(int num)  
{   
   int curr_mult = 10;
   int tmpNum = num;
   int val;
   int c = 1;
   int ret = 0;
   for (int i = 0; i < 16; i++)
   {
       val = tmpNum % 10;
       if (val % 2 == 0)
       {
           ret += c*val;
           c *= 10;
       }
       tmpNum = tmpNum/10;
   }
   
   if (ret == 0) return -1;
   
   return ret;
}
void extEvenDigits2(int num, int *result)  
{   
   int curr_mult = 10;
   int tmpNum = num;
   int val;
   int c = 1;
   int ret = 0;
   for (int i = 0; i < 16; i++)
   {
       val = tmpNum % 10;
       if (val % 2 == 0)
       {
           ret += c*val;
           c *= 10;
       }
       tmpNum = tmpNum/10;
   }
    if (ret == 0) 
    {
        *result = -1;
    }
    else
    {
        *result = ret;
    }
}
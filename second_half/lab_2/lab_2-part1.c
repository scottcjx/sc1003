#include <stdio.h>
int numDigits1(int num);
void numDigits2(int num, int *result);
int main()
{
   int number, result=0;
    
   printf("Enter the number: \n");
   scanf("%d", &number);
   printf("numDigits1(): %d\n", numDigits1(number));    
   numDigits2(number, &result);
   printf("numDigits2(): %d\n", result);            
   return 0;
}
int numDigits1(int num)
{
   /* Write your code here */
    int c = 1;
    for (int i = 1; num/i >= 10; c++)
    {
        i *= 10;
    }
    return c;
}
void numDigits2(int num, int *result)
{
   /* Write your code here */
    // int c = 1;
    // for (int i = 1; num/i >= 10; c++)
    // {
    //     i *= 10;
    // }

    // *result = c;

    *result = numDigits1(num);
}
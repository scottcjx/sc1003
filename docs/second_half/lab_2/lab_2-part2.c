#include <stdio.h>
int digitPos1(int num, int digit);
void digitPos2(int num, int digit, int *result);
int main()
{
   int number, digit, result=0;
   printf("Enter the number: \n");
   scanf("%d", &number);
   printf("Enter the digit: \n");
   scanf("%d", &digit);             
   printf("digitPos1(): %d\n", digitPos1(number, digit));            
   digitPos2(number, digit, &result);           
   printf("digitPos2(): %d\n", result);    
   return 0;
}
void numDigits(int num, int *result)
{
   /* Write your code here */
    int c = 1;
    for (int i = 1; num/i >= 10; c++)
    {
        i *= 10;
    }

    *result = c;
}
int digitPos1(int num, int digit)  
{
    /* Write your code here */
    int num_length;
    numDigits(num, &num_length);

    for (int i = 0; i < num_length + 1; i++)
    {
        int r = num / pow(10, i);
        r = r % 10;
        
        if (r == digit)
        {
            return i;
        }
    }

    return num_length;
}
void digitPos2(int num, int digit, int *result)  
{
   /* Write your code here */
   *result = digitPos1(num, digit);
}

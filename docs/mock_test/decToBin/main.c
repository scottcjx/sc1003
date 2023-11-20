#include <stdio.h>
#include <math.h>
int main()
{
 int req_num;
 printf("Enter a decimal number:\n");
 scanf(" %d", &req_num);
 
 printf("The equivalent binary number: ");
 
 int need_bits = ((int) log2(req_num)) + 1;
 int curr_num = req_num;
 int curr_mult;
 
 for(int i = need_bits - 1; i > -1; i--)
 {
    curr_mult = (int) pow(2,i);
    if (curr_mult <= curr_num)
    {
        printf("1");
        curr_num -= curr_mult;
    }
    else
    {
        printf("0");
    }
 }
 printf("\n");
 return 0;
} 

# Further Pratice octStrToDec

## Content
``` c
#include <stdio.h>

int char2dec(char c)
{
    switch(c)
    {
        case '0': return 0;
        case '1': return 1;
        case '2': return 2;
        case '3': return 3;
        case '4': return 4;
        case '5': return 5;
        case '6': return 6;
        case '7': return 7;
        case '8': return 8;
        case '9': return 9;
    }
    return 0;
}
int octStrTodec(char *str);

int main()
{
 char str[20],*sp;
 int num;

 printf("Enter an octal number: \n");
 scanf("%s",str);
 num=octStrTodec(str);
 printf("octStrTodec(): %d\n",num);
 return 0;
}
int octStrTodec(char *str)
{
 int len = strlen(str);
   int curr_sum = 0;
   int curr_mult = 1;
   int curr_num;
   for (int i = len - 1; i > -1; i--)
   {
       curr_num = char2dec(str[i]);
       curr_sum += (curr_num) * curr_mult;
       curr_mult *= 8;
   }
   
   return curr_sum;

}
```
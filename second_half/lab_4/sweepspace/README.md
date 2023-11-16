# Sweepspace

## Contents

### using array
``` c
char *sweepSpace1(char *str)   
{
   /* Write your program code here */
   char *tstr = malloc(80);
   int curr_pos = 0;
    
   for (int i = 0; i < strlen(str); i++)
   {
        
       if (str[i] != ' ')
       {
           tstr[curr_pos] = str[i];
           curr_pos++;
       }
   }
   return tstr;
}
```

### using pointers
``` c
char *sweepSpace2(char *str)   
{
   /* Write your program code here */
   char *tstr = malloc(80);
   int curr_pos = 0;
    
   for (int i = 0; i < strlen(str); i++)
   {
       if (*(str + i) != ' ')
       {
           *(tstr + curr_pos) = *(str + i);
           curr_pos++;
       }
   }
   return tstr;
}
```
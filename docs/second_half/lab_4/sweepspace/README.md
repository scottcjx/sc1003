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

## License
This project is available under the GPL v3 license. See the [LICENSE](./LICENSE.md) file for more info.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

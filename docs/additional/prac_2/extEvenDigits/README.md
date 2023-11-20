# extEvenDigits

## by return
``` c
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
```

## by pointer
``` c
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
```

## License
This project is available under the GPL v3 license. See the [LICENSE](./LICENSE.md) file for more info.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

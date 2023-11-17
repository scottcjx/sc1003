# Functions and Pointers

## Contents

- [Part 1](./lab_2-part1.c)
- [Part 2](./lab_2-part2.c)

#### numDigits
``` c
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
```

#### digitPos1
``` c
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
```

#### digitPos2
``` c
void digitPos2(int num, int digit, int *result)  
{
   /* Write your code here */
   *result = digitPos1(num, digit);
}
```

## License
This project is available under the GPL v3 license. See the [LICENSE](./LICENSE.md) file for more info.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

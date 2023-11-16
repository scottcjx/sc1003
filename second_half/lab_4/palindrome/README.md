# Palindrome

## Contents

``` c
int palindrome(char *str)
{
    /* Write your code here */
    int len_str = strlen(str);

    for (int i = 0; i < len_str / 2; i++)
    {
        if (str[i] != str[(len_str - 1) - i]) return 0;
    }
    return 1;
}
```

## License
This project is available under the GPL v3 license. See the [LICENSE](./LICENSE.md) file for more info.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

# Tutorial 4

``` c
int stringcmp(char *s1, char *s2)
{
   int strcmp_ret = strcmp(s1, s2);
   if (strcmp_ret == 0) return 0;
   else if (strcmp_ret > 0) return 1;
   else if (strcmp_ret < 0) return -1;
   return -2;
}
```

## License
This project is available under the GPL v3 license. See the [LICENSE](./LICENSE.md) file for more info.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

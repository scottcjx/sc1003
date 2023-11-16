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
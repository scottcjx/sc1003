# stringncpy

``` c
char *stringncpy(char *s1, char *s2, int n)
{
    for (int i = 0; i < n; i++)
   {
       s1[i] = s2[i];
   }
   s1[n] = '\0';
   
   return s1;
}
```
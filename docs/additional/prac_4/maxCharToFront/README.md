# MaxCharToFront

``` c
void maxCharToFront(char *str)  
{
   int len = strlen(str);
   int idx_max = 0;
   for (int i = 0; i < len; i++)
   {
       if (str[i] > str[idx_max]) idx_max = i;
   }
   
   if (idx_max == 0) return;
   
    char* tmpStr = malloc(sizeof(str));
  strcpy(tmpStr, str);
   
  tmpStr[0] = str[idx_max];
  
  for (int i = 0; i <= idx_max-1; i++)
  {
      tmpStr[i+1] = str[i];
  }
  strcpy(str, tmpStr);
}
```
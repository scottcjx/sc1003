# Cipher Text

### Cipher
``` c
void cipher(char *s)   
{
   int len = strlen(s);
   for (int i = 0; i < len; i++)
   {
      if (isalpha(s[i]))
      {
          if (s[i] == 'z')
          {
              s[i] = 'a';
          }
          else if (s[i] == 'Z')
          {
              s[i] = 'A';
          }
          else
          {
              s[i]++;
          }
      }
   }
}
```

### Decipher

``` c
void decipher(char *s)   
{
   int len = strlen(s);
   for (int i = 0; i < len; i++)
   {
      if (isalpha(s[i]))
      {
          if (s[i] == 'a')
          {
              s[i] = 'z';
          }
          else if (s[i] == 'A')
          {
              s[i] = 'Z';
          }
          else
          {
              s[i]--;
          }
      }
   }
}
```

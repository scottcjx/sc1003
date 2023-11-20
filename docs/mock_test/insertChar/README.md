# insertChar

[Read the Brief](./insertChar.pdf)


## Contents

``` c
void insertChar(char *str1, char *str2, char ch)
{
  int len = strlen(str1);
  char tmpStr[len];
  int times_add = (len / 3);
  int j = 0;
  int add_counter = 0;
  for (int i = 0; i < len + times_add; i++)
  {
      if (add_counter >= 3)
      {
          tmpStr[i] = ch;
          add_counter = 0;
      }
      else
      {
          tmpStr[i] = str1[j];
          add_counter++;
          j++;
      }
  }

  strcpy(str2, tmpStr);
}
```

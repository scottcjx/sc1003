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
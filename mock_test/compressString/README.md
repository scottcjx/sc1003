# CompressString

[Read the brief](./compressStr.pdf)

``` c
void compressStr(char *str)
{
    int len = strlen(str);
    int cont_char_count = 0;
    char prev_char = 0;

    if (len == 1)
    {
        printf("%c", str[0]);
        return;
    }

    for (int i = 0; i < len + 1; i++)
    {
        if (prev_char == str[i])
        {
            cont_char_count++;
        }
        else
        {
            if (cont_char_count == 0)
            {
                
            }
            else if (cont_char_count == 1)
            {
                printf("%c", prev_char);
            }
            else 
            {
                printf("[%d%c]", cont_char_count, prev_char);
            }
            cont_char_count = 1;
        }
        prev_char = str[i];
    }
}
```
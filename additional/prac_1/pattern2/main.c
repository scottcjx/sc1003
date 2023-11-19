#include <stdio.h>
int main()  
{
    const char chars[] = { 'A', 'B' };
    int curr_char = 0;

    int req_height;
    printf("Enter the height: \n");
    scanf(" %d", &req_height);

    printf("The pattern is: \n");
    for (int i = 1; i < req_height + 1; i++)
    {
        curr_char = (i % 2) ? 0 : 1;
        for (int j = 0; j < i; j++)
        {
            printf("%c", chars[curr_char]);
            if (curr_char == 0) curr_char++;
            else curr_char--;
        }
        printf("\n");
    }
   return 0;
}
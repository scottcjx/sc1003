#include <stdio.h>
#include <string.h>
void insertChar(char *str1, char *str2, char ch);
int main()  
{
   char a[80],b[80];
   char ch, *p;
    
   printf("Enter a string: \n");   
   fgets(a, 80, stdin);
   if (p=strchr(a,'\n')) *p = '\0';  
   printf("Enter a character to be inserted: \n");   
   ch = getchar();
   insertChar(a,b,ch);
   printf("insertChar(): ");   
   puts(b);      
   return 0;
}
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
#include <stdio.h>
int main()  
{
  int usr_inp = 0;
  double converted_val = 0;

  while (usr_inp != -1)
  {
    printf("Enter the temperature in degree F: \n");
    scanf(" %d", &usr_inp);
    
    if (usr_inp == -1) return 0;
    
    converted_val = (usr_inp - 32) * (5.00/9.00);
    printf("Converted degree in C: %.2f\n", converted_val);

  }
  
  return 0;
}

const char GRADES[] = {'A', 'B', 'C', 'D', 'F'};

char get_grade(int user_score)
{
    if (user_score < 0)
   {
    //   error
        return GRADES[4];
   }
   else if (user_score < 45)
   {
       return GRADES[4];
   }
   else if (user_score < 55)
   {
       return GRADES[3];
   }
   else if (user_score < 65)
   {
       return GRADES[2];
   }
   else if (user_score < 75)
   {
       return GRADES[1];
   }
   else if (user_score <= 101)
   {
       return GRADES[0];
   }
}

int main()
{
 /* Write your code here */
   int user_id;
   int user_input;
  do
  {
        printf("Enter Student ID:\n");
        scanf("%d ", &user_id);
       
        if (user_input == -1)
        {
            //   printf("ending...");
            return 0;
        }
       
        printf("Enter Mark: \n");
        scanf("%d ", &user_input);
        printf("Grade = %c \n", get_grade(user_input));
       
  } while (1);

  return 0;
}


const char GRADES[] = {'A', 'B', 'C', 'D', 'F'};

char get_grade(int user_score)
{
    // catch that scores are less than or equal to 0
    if (user_score <= 0)
    {
        return GRADES[-1];
    }

    // aggregate score from 0 - 100 to 5 - 105
    int agg_score = user_score + 5;

    // divide scores to intervals of 10.
    // 0 - 45 = 0-4, 45 - 55 = 5, 55 - 65 = 6, 65 - 75 = 7... 
    int num_grade = agg_score / 10;

    switch (num_grade)
    {
        case 10:
            // agg: 100-105, raw: 95 - 100
        case 9:
            // agg: 90 - 99, raw: 85 - 95
        case 8:
            // agg: 80 - 89, raw: 75 - 85
            return GRADES[0];
            break;
        case 7:
            return GRADES[1];
            break;
        case 6:
            return GRADES[2];
            break;
        case 5:
            return GRADES[3];
            break;
        case 4:
            return GRADES[4];
            break;
        default:
            return GRADES[4];
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

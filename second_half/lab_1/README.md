# Control Flow

## Contents
- [using if statement](./lab_1_computeGrade.c)
- [using switch statement](./lab_1_computeGrade.c) (requested by lab manual)

#### using If
``` c

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

```

#### using Switch

``` c
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
```

## License
This project is available under the GPL v3 license. See the [LICENSE](./LICENSE.md) file for more info.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

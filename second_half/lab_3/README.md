# Arrays

## Contents

- [Part 1](./lab_3-1.c)
- [Part 2](./lab_3-2.c)
- [Part 3](./lab_3-3.c)


### Part 2

#### Displaying
``` c
void display(int ar[][SIZE])
{
   int l,m;
   for (l = 0; l < SIZE; l++) {
      for (m = 0; m < SIZE; m++)
         printf("%d ", ar[l][m]);
      printf("\n");
   }
}
```

#### Swap 2 Rows
``` c
void swap2Rows(int ar[][SIZE], int r1, int r2)
{
   int bufVal;
   for (int i = 0; i < SIZE; i++)
   {
       bufVal = ar[r1][i];
       ar[r1][i] = ar[r2][i];
       ar[r2][i] = bufVal;
   }
}
```

#### Swap 2 Cols
``` c
void swap2Cols(int ar[][SIZE], int c1, int c2)
{
   int bufVal;
   for (int i = 0; i < SIZE; i++)
   {
       bufVal = ar[i][c1];
       ar[i][c1] = ar[i][c2];
       ar[i][c2] = bufVal;
   }
}
```

### Part 3

#### Reversing 1D Array

``` c
void reverseAr1D(int ar[], int size)
{
    int bufArr[size];

    // Copy contents of ar into bufArr
    // inbuilt function for this OR:
    memcpy(bufArr, ar, sizeof(int)*size);

    // manual function for this application
    // for (int i = 0; i < size; i++)
    // {
    //     bufArr[i] = ar[i];
    // }

    // iterate through the array contents
    for (int i = 0; i < size; i++)
    {
        // set the i-th index of ar to the i-th val (from the back) since 
        // elements are 0 indexed, [size-1] would give index of LAST element
        // [size-1]-i will give the i-th element from the back of the array
        ar[i] = bufArr[(size-1)-i];

        // therefore assigning ar[i] to ar[last-i] to reveres the positions of the
        // elements in the array.
    }
} 
```

## License
This project is available under the GPL v3 license. See the [LICENSE](./LICENSE.md) file for more info.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

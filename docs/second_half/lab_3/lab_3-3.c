#include <stdio.h>
void reverseAr1D(int ar[], int size);
int main()
{
    int ar[10];
    int size, i;

    printf("Enter array size: \n");
    scanf("%d", &size);
    printf("Enter %d data: \n", size);
    for (i=0; i <= size-1; i++)
    scanf("%d", &ar[i]);
    reverseAr1D(ar, size);
    printf("reverseAr1D(): ");
    if (size > 0) {
    for (i=0; i<size; i++)
    printf("%d ", ar[i]);
    }
    return 0;
}
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
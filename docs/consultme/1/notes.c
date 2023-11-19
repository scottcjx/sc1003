
// final assignment

// arrays + pointers
// structs
// struct pointer ref 
// functions pass by (value, reference)
// strings x

// arrays + pointers 1/2
// arrays x

int arr [5] = { 0, 1, 2, 3, 4 };
//       ^.     
//  idx:        0  1  2  3  4 <-
// zero indexed ^
// sizeof arr/ strlen NUMBER of elements in an array.
// zero indexed arr, idx of last element is (strlen - 1)
// last element can also be index -1 (we will find out)

    printf(" %d", arr[0]);  // 0
    printf(" %d", arr[3]);  // 3

    // 4rd element is 3rd <- zero index

int *pArr;
//  ^ pointer definition; type: (int*) <- pointer to an integer

// keep in view (KIV)
{
    // arrays are pointers
    // they point to the FIRST ELEMENT, ZEROTH index of the array
    printf(" %d", arr);         // the address of the array
                                // the address of the FIRST ELEMENT in the array
    pArr = arr;                 // an array on its own IS a pointer
    printf(" %d", pArr);        // the address of the array
}

/* strings */
// strings are essentially char arrays 
// string can be defined as 

const int LEN_OF_STR = 80;
char myStr[LEN_OF_STR];
//          ^ myStr/ Stirngs in general are arrays
//          ALL arrays are pointers
//  p -> q -> s
//  p -> s

char myStr[LEN_OF_STR];     // is the same as 
char *pMyStr;

pMyStr = malloc(sizeof(char) * 10);
//      give me a block of memory 
//      with size 10 * sizeof(char) 10 * 1 = 10 blocks
//      returns a pointer to FIRST element of chunk.

strcpy(pMyStr, "Hello");

// Hello -> HELLO

// string char iteration:
for(int i = 0; i < strlen(pMyStr); i++)
{
    // processing info
    myChar = toupper(pMyStr[i]);

    // important concept for pointers
    pMyStr[i] 
    // same as 
    *(pMyStr + i)

    // custom datatype
    // made of native datatypes
    // int float char double
}

// the only difference is that an array has 

// varaibles are stored in blocks of memories
// within RAM.

// 2D arrays
int arr2d[][];
//       ^ ^ 2D
//       ^ 1D


int arr[2][] = { int[], int[]};
// same as ^
int my2darr[][] = { 
    {1, 2, 3, 4, 5}, 
    {6, 7, 8, 9, 10}
};

my2darr[0]  // <- first element
//  => {1, 2, 3, 4, 5} => type: int[]
//  => ^ address of the first element in the array

int *pInt;
pInt = &my2darr;
// pInt = &(1^);

for (int i = 0; i < rows; i++)
{
    // rows
    for (int j = 0; j < cols; j++)
    {
        // cols
        printf("(%d, %d)", i ,j);
    }
}

// structs

// define my own datatype.
typedef struct
{
    int ID;
    int time_created;
} myType;


// * can use a custom datatype (struct)
// as a datatype in another struct
typedef struct
{
    struct myType myVar;
} Person;

typedef struct
{
    char name[40];
    char title[40];         // (char*)
    int id;
} Employee;


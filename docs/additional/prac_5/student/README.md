# Student

### inputStud
``` c
void inputStud(Student *s, int size)  
{
    for (int i = 0; i < size; i++)
    {
        printf("Student ID: \n");
        scanf(" %d", &s[i].id);
        printf("Student Name: \n");
        scanf(" %[^\n]s", s[i].name);
    }
}
```

### printStud
``` c
void printStud(Student *s, int size)  
{
    printf("The current student list:\n");
    
    if (size == 0)
    {
        printf("Empty array\n");
        return;
    }
    
    for (int i = 0; i < size; i++)
    {
        printf("Student ID: %d ", s[i].id);
        printf("Student Name: %s\n", s[i].name);
    }
}
```

### removeStud
``` c
int removeStud(Student *s, int *size, char *target)  
{
    if ((*size) == 0) return 1;
    
    for (int i = 0; i < *size; i++)
    {
        if(strcmp(s[i].name, target) == 0)
        {
            s[i] = (Student) {};
            (*size)--;
            return 0;
        }
    }
    return 2;
}
```
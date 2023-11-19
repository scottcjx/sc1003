# Employee

## Contents

### readin
``` c
int readin(Employee *emp)
{
 Employee tmpEmp;
   
   int num_emp = 0;
    for(int i = 0; i < MAX; i++)
   {
        printf("Enter name: \n");
        scanf(" %[^\n]s", tmpEmp.name);
        
        // how to break;
        if (strcmp(tmpEmp.name, "#") == 0)
        {
            break;
        }
        
        printf("Enter tel: \n");
        scanf(" %[^\n]s", tmpEmp.telno);
        
        printf("Enter id: \n");
        scanf(" %d", &tmpEmp.id);
        printf("Enter salary: \n");
        scanf(" %lf", &tmpEmp.salary);
        
        // copy tmpBuffer to arr
        memcpy( (emp+num_emp), &tmpEmp, sizeof(Employee) );
        num_emp ++;
   }
   
   return num_emp;

}
```

### search
``` c
int search(Employee *emp, int size, char *target)
{
 for (int i = 0; i < size; i++)
   {
    //   *(emp+i) => (Employee)  <= value
    //    (emp+i) => (&Employee) <= pointer
    // i want this      emp[i].name
    //    (emp+i)
    //    (emp+i)->name;
       
       if (strcmp(target, (emp+i)->name) == 0)
       {
           printf("Employee found at index location: %d\n", i);
           printf("%s %s %d %.2f\n", (emp+i)->name , (*(emp+i)).telno, emp[i].id, (emp[i]).salary); 
           return i;
       }
   }
}
```

### addEmployee
``` c
int addEmployee(Employee *emp, int size, char *target)
{
 if (size >= MAX)
    {
        printf("Database is full\n");
        return size;
    }
    
    // 1. check if name exists in emp arr
    // 2. add target into (last element of arr)
    
    for (int i = 0; i < size; i++)
    {
        if(strcmp(emp[i].name, target) == 0)
        {
            // name exists in database
            return size;
        }
    }
    
    // assumptions are:
    // 1. size is within range
    // 2. target is a valid target
    
    // add this target to database
    
    Employee tmpBuf;
    
    printf("Enter tel:\n");
    scanf(" %[^\n]s", tmpBuf.telno);
    
    printf("Enter id:\n");
    scanf(" %d", &tmpBuf.id);
    
    printf("Enter salary:\n");
    scanf(" %lf", &tmpBuf.salary);
    
    // add tmpBuf to last element of my emparr.
    // given size of emp arr BEFORE addition.
    // zero-th index prog.
    // size
    // sizeof arr = 10 => last element @ 9 (9 is populated)
    
    strcpy(emp[size].name, target);
    strcpy(emp[size].telno, tmpBuf.telno);
    emp[size].id = tmpBuf.id;
    emp[size].salary = tmpBuf.salary;
    
    printf("Added at position: %d\n", size);
    
    return size + 1;
}
```
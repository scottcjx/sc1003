#include <stdio.h>
#include <string.h>
#define MAX 100
typedef struct {
 char name[40];
 char telno[40];
 int id;
 double salary;
} Employee;
void printEmp(Employee *emp, int size);
int readin(Employee *emp);
int search(Employee *emp, int size, char *target);
int addEmployee(Employee *emp, int size, char *target);
int main()
{
 Employee emp[MAX];
 char name[40], *p;
 int size, choice, result;

 printf("Select one of the following options: \n");
 printf("1: readin() \n");
 printf("2: search() \n");
 printf("3: addEmployee() \n");
 printf("4: print() \n");
 printf("5: exit() \n"); 
do {
 printf("Enter your choice: \n");
 scanf("%d", &choice);
 switch (choice) {
 case 1:
 size = readin(emp);
 break;
 case 2:
 printf("Enter search name: \n");
 scanf("\n");
 fgets(name, 40, stdin);
 if (p=strchr(name,'\n')) *p = '\0';
 result = search(emp,size,name);
 if (result != 1)
 printf ("Name not found! \n");
 break;
 case 3:
 printf("Enter new name: \n");
 scanf("\n");
 fgets(name, 40, stdin);
 if (p=strchr(name,'\n')) *p = '\0';
 result = search(emp,size,name);
 if (result != 1)
 size = addEmployee(emp, size, name);
 else
 printf("The new name has already existed in the database\n");
 break;
 case 4:
 printEmp(emp, size);
 break;
 default:
 break;
 }
 } while (choice < 5);
 return 0;
}
void printEmp(Employee *emp, int size)
{
 int i;

 printf("The current employee list: \n");
 if (size==0)
 printf("Empty array\n");
 else
 {
 for (i=0; i<size; i++)
 printf("%s %s %d %.2f\n",emp[i].name,emp[i].telno,emp[i].id,
 emp[i].salary);
 }
}
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
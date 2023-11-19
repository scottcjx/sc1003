#include <stdio.h>
typedef struct {
 char name[20];
 int age;
} Person;
void readData(Person *p);
Person findMiddleAge(Person *p);
int main()
{
 Person man[3], middle;

 readData(man);
 middle = findMiddleAge(man);
 printf("findMiddleAge(): %s %d\n", middle.name, middle.age);
 return 0;
}
void readData(Person *p)
{
    for (int i = 0; i < 3; i++)
    {
        printf("Enter person %d:\n", i+1);
        scanf(" %s %d", p[i].name, &p[i].age);
    }
}
Person findMiddleAge(Person *p)
{
    int idx_min = 0;
	int idx_max = 0;
	for (int i = 1; i < 3; i++)
	{
	    if (p[i].age < p[idx_min].age) idx_min = i;
	    if (p[i].age > p[idx_max].age) idx_max = i;
	}
	
	for (int i = 0; i < 3; i++)
	{
	    if (idx_min != i && idx_max != i) return p[i];
	}
} 
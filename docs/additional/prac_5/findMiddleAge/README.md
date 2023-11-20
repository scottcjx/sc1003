# findMiddleAge

## Contents

### Read Data
``` c
void readData(Person *p)
{
    for (int i = 0; i < 3; i++)
    {
        printf("Enter person %d:\n", i+1);
        scanf(" %s %d", p[i].name, &p[i].age);
    }
}
```

### findMiddleAge
``` c
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
```

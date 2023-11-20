# customer

### nextCustomer
``` c
void nextCustomer(struct account *acct)    
{   
    printf("Enter names (firstName lastName):\n");
	scanf(" %s %s", acct->names.firstName, acct->names.lastName);
	printf("Enter account number:\n");
	scanf(" %d", &acct->accountNum);
	printf("Enter balance:\n");
	scanf(" %lf", &acct->balance);
}
```

### printCustomer
``` c
void printCustomer(struct account acct)    
{   
	printf("Customer record: \n");
	printf("%s %s %d %.2f\n", acct.names.firstName, acct.names.lastName, acct.accountNum, acct.balance);
}
```

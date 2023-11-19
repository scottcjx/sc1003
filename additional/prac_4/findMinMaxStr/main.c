#include <stdio.h>
#include <string.h>
#define SIZE 10
void findMinMaxStr(char word[][40], char *first, char *last, int size);
int main()
{
   char word[SIZE][40];
   char first[40], last[40];
   int i, size;  
    
   printf("Enter size: \n");
   scanf("%d", &size);
   printf("Enter %d words: \n", size);
   for (i=0; i<size; i++)
      scanf("%s", word[i]);  
   findMinMaxStr(word, first, last, size);   
   printf("First word = %s, Last word = %s\n", first, last);         
   return 0;
}

void findMinMaxStr(char word[][40], char *first, char *last, int size)
{
    int btr_ranked;
	int ranks[size];
	for (int i = 0; i < size; i++)
	{
	    btr_ranked = 0;
	    for (int j = 0; j < size; j++)
	    {
	        if (strcmp(word[i], word[j]) > 0) btr_ranked++;
	    }
	    ranks[btr_ranked]= i;
	}
	
// 	^ some real advanced shit. pm me for help
	
// 	printf("rank %d:%s\n", 0, word[ranks[0]]);
// 	printf("rank %d:%s\n", size-1, word[ranks[size-1]]);
	
	strcpy(first, word[ranks[0]]);
	strcpy(last, word[ranks[size-1]]);
}
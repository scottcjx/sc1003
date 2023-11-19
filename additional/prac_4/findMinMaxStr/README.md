# findMinMaxStr
``` c
void findMinMaxStr(char word[][40], char *first, char *last, int size)
{
    int btr_ranked;
	int ranks[size];
	for (int i = 0; i < size; i++)
	{
	    btr_ranked = 0;
        
        // compare word[i] to every word in word arr;
	    for (int j = 0; j < size; j++)
	    {
            // count number of strings word[i] is better ranked than
	        if (strcmp(word[i], word[j]) > 0) btr_ranked++;
	    }
        
        // assuming there is no duplicates,
        // use array as a hashmap per se
        // the rank of word[i] is the number of strings it is better ranked in.
	    ranks[btr_ranked]= i;
	}
	
// 	^ some real advanced shit. pm me for help
	
// 	printf("rank %d:%s\n", 0, word[ranks[0]]);
// 	printf("rank %d:%s\n", size-1, word[ranks[size-1]]);
	
	strcpy(first, word[ranks[0]]);
	strcpy(last, word[ranks[size-1]]);
}
```
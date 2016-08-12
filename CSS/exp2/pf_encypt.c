#include <stdio.h>
#include <string.h>

char custom_input()
{
	char c;
	char arr[100];
	int len = 0;

	while(1)
	{
	} 
}

int main()
{
	//key is "cipher"
	char square[5][5] = {{'c','i','p','h','e'},{'r','a','b','d','f'},{'g','k','l','m','n'},{'o','q','s','t','u'},{'v','w','x','y','z'}};
	char input_text[100];
	char *input_pointer;
	//char digraph_array[1]; declaration later on
	int i,j; //iteration vars
	int len;
	
	scanf("%s",input_text);
//	custom_input(input_pointer); //not working
	//puts(input_text);
	len = strlen(input_text);
	
	int x=0;
	if (len%2 == 0)
	{
		x = len/2;
	}
	else
	{
		x = (len+1)/2;
	}
	
	char digraph_array[len/2][2];
	int counter = 0;
	for (i = 0; i < len/2; i++)
	{
		for (j = 0; j < 2; j++)
		{
			//printf("-%c",input_text[counter]);
			digraph_array[i][j] = input_text[counter];
			counter++;
		}
	}

/** //working	
	for (i = 0; i < len/2; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("%c ",digraph_array[i][j]);
		}
	}
**/	
	
	return(0);
}

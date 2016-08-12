#include<stdio.h>
/**
Mathematical operations
-> Addition
-> Scaling
-> Multiplication
**/

struct signal
{
	int list[100];
	int len;
	int origin;
};

int menu()
{
	int choice = 0;
	
	printf("\n :: MENU :: \n");
	printf(" 1 - Addition\n");
	printf(" 2 - Scaling\n");
	printf(" 3 - Multiplication\n");
	printf(" 4 - Exit\n");
	
	while (choice < 1 && choice > 3)
	{
		printf("-> ");
		scanf("%d",&choice);
		
		if (choice < 1 || choice > 4)
		{
			printf(" :: Bad input!\n");
		}
	}
	
	return(choice);
}

int addition(struct signal s1)
{
	struct signal s2;	
	int i;
	
	printf("\n :: ADDITION ::\n");
	
	printf("Length of signal : ");
	scanf("%d",&s2.len);
	printf("\n");
	
	printf(" :: Signal values :: \n");
	for (i = 0; i < s2.len; i++)
	{
		printf("Signal[%d] : ",i);
		scanf("%d",&s2.list[i]);
	}
	
	s2.origin = 99;
	while (s2.origin >= 0 && s2.origin < len)
	{
		printf("\nIndex for origin : ");
		scanf("%d",&s2.origin);
	}
	
	if (s1.len > s2.len)
	{
		if (s1.origin < s2.origin)
		{
			i = len;
			while (s1.origin != s2.origin)
			{
				s1.list[i-1] = s1.list[i];
				i--;
			}
			//TODO continue here
		}
	}
	else if (s1.len < s2.len)
	{
		
	}
	else
	{
		
	}
}

void main()
{
	struct signal s1;
	int i,j; //iteration vars
	bool loop = true;
	
	printf("Length of signal : ");
	scanf("%d",&s1.len);
	printf("\n");
	
	printf(" :: Signal values :: \n");
	for (i = 0; i < s1.len; i++)
	{
		printf("Signal[%d] : ",i);
		scanf("%d",&s1.list[i]);
	}
	
	s1.origin = 99;
	while (s1.origin >= 0 && s1.origin < len)
	{
		printf("\nIndex for origin : ");
		scanf("%d",&s1.origin);
	}
	
	while (loop == true)
	{
		switch(menu()):
		{
			case 1: //addition
				addition(s1);
			break;
			
			case 2: //Scaling
			break;
			
			case 3: //Multiplication
			break;
			
			case 4: //Exit
			loop = False;
			break;
			
			default:
			printf("\n :: How'd you get here?!\n");
			break;
		}
	}	
		
	return;
}

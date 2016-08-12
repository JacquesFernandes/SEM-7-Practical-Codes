#include<stdio.h>
#include<string.h>

char convert(char in, int shift)
{	
	if (in == ' ')
	{
		return('@');
	}
	int ano = (int)in; //ASCII no.
	int cno = ano-97; //"scaling" numbers e.g. a=>97-97 => 0 // A=>65 // 97-65 = 32 // lower -32 = upper
	ano = (cno+shift)%26 + 97;
	//printf("\n%c = %d",in,ano);
	char op = (char)(ano-32);
	return(op);
}

int main()
{
	char inp[100] = "";
	char op[100] = "";
	int len = 0;
	char c;
	int shift_key;
	
	printf("Enter the String: ");
	int i = 0;
	while ((c = getchar()) != '\n')
	{
		*(inp+i) = c;
		i++;
	}
	*(inp+i+1) = '\0';
	len = i;
	
	printf("Enter the Key: ");
	scanf("%d",&shift_key);
	
	for (i = 0; i < len; i++)
	{
		c = convert(inp[i],shift_key);
		if (c == '@')
		{
			i--;
		}
		else
		{
			op[i] = c;
		}
	}
	
	//printf("%s",op);
	
	FILE *fp = fopen("op.txt","w+");
	fprintf(fp,"%s",op);
	fclose(fp);
	printf("\nDone, check op.txt");
	return(0);
}

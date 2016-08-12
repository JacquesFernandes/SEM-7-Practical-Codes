#include<stdio.h>
#include<string.h>

char convert(char in, int shift)
{
	int ano = (int)in; //ASCII no.
	int cno = ano-65; //"scaling" numbers e.g. a=>97-97 => 0 // A=>65 // 97-65 = 32
	ano = (cno-shift+26)%26 + 65;
	//printf("\n%c = %d",in,ano);	
	char op = (char)(ano+32);
	return(op);
}

int main()
{
	FILE *fp = fopen("op.txt","r");
	char inp[100]="";
	char op[100]="";
	int key,len;
	
	fscanf(fp,"%s",inp);
	fclose(fp);
	
	printf("Enter the key: ");
	scanf("%d",&key);
	
	len = strlen(inp);
	
	int i;
	for(i = 0; i < len; i++)
	{
		op[i] = convert(inp[i],key);
	}
	
	printf("\nEncrypted : %s",inp);
	printf("\nDecrypted : %s",op);
	
	return(0);
}

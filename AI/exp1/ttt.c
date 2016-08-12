#include<stdio.h>
int winner(int);
int enter(int,int);
int cur(void);
int pos,counter=0;
int a[3][3];

int cur()
{
int i,j;
//showing current state
printf("\nGame board after entering your turn!:");
	for(i=0;i<3;i++)
	{
		printf("\n");
		for(j=0;j<3;j++)
		{
			printf("%d ",a[i][j]);
		}
	}
return 0;
}

int main()
{
	int b[3][3],i,j,k=0,z;
	printf("\t\t\tTIC TAC TOE\n");//DISPLAY
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			b[i][j]=++k;
		}
		printf("These are the positions:\n");
		for(i=0;i<3;i++)
		{
			printf("\n");
			for(j=0;j<3;j++)
			{
				printf("%d ",b[i][j]);
			}
		}
	
	//initializing matrix
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			a[i][j]=5;}//ASKING FOR INPUT
			for(z=1;z<=9;z++)
			{//Player 1
				if(z%2!=0)
				{
					printf("\nPlayer 1 enter your choice of position:");
					scanf("%d",&pos);
					enter(1,pos);
					cur();
					winner(pos);
					if(counter>0)
					{
						break;
					}
				}
				else
				{
					printf("\nPlayer 2 enter your choice of position:");
					scanf("%d",&pos);
					enter(2,pos);
					cur();
					winner(pos);
					if(counter>0)
					{
						break;
					}
				}
			}
			if(counter==0)
			{
				printf("Match is draw!");
			}
		}
	}
}

//ENTERING VALUES
int enter(int p,int pos)
{
	if(pos==1){
	a[0][0]=p;}
	if(pos==2){
	a[0][1]=p;}
	if(pos==3){
	a[0][2]=p;}
	if(pos==4){
	a[1][0]=p;}
	if(pos==5){
	a[1][1]=p;}
	if(pos==6){
	a[1][2]=p;}
	if(pos==7){
	a[2][0]=p;}
	if(pos==8){
	a[2][1]=p;}
	if(pos==9){
	a[2][2]=p;
	}return 0;}//finding out winner
int winner(int pos){
if(pos == 1){
//Horizontal
if (a[0][0] == a[0][1] && a[0][0] == a[0][2]){
if(a[0][0] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}//Vertical
if(a[0][0] == a[1][0] && a[0][0] == a[2][0]){
if(a[0][0] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//diagonal
if(a[0][0] == a[1][1] && a[0][0] == a[2][2]){
if(a[0][0] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}}
if(pos == 2){
//Horizontal
if (a[0][0] == a[0][1] && a[0][0] == a[0][2]){
if(a[0][1] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//Vertical
if(a[0][1] == a[1][1] && a[0][1] == a[2][1])
{if(a[0][1] == 1){
printf("Player 1 wins!\n");
counter++;}else{
printf("Player 2 wins!\n");
counter++;}}}
if(pos == 3){
//Horizontal
if (a[0][0] == a[0][1] && a[0][0] == a[0][2]){
if(a[0][2] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//Vertical
if(a[0][2] == a[1][2] && a[0][2] == a[2][2]){
if(a[0][2] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//diagonal
if(a[0][2] == a[1][1] && a[0][2] == a[2][0]){
if(a[0][2] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}}
if(pos == 4){
//Horizontal
if (a[1][0] == a[1][1] && a[1][0] == a[1][2]){
if(a[1][0] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}//Vertical
if(a[0][0] == a[1][0] && a[1][0] == a[2][0]){
if(a[1][0] == 1){
printf("Player 1 wins!\n");counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}}
if(pos == 5){
//Horizontal
if (a[1][0] == a[1][1] && a[1][0] == a[1][2]){
if(a[1][1] == 1)
{printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//Vertical
if(a[0][1] == a[1][1] && a[1][1] == a[2][1]){
if(a[1][1] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//diagonal
if(a[0][0] == a[1][1] && a[1][1] == a[2][2]){
if(a[0][0] == 1)
{printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//diagonal 2
if(a[0][2] == a[1][1] && a[1][1] == a[2][0]){
if(a[0][0] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}}
if(pos == 6){
//Horizontal
if (a[1][0] == a[1][2] && a[1][2] == a[1][1]){if(a[1][2] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//Vertical
if(a[0][2] == a[1][2] && a[1][2] == a[2][2]){
if(a[1][2] == 1){
printf("Player 1 wins!\n");
counter++;
}else{
printf("Player 2 wins!\n");
counter++;}}}
if(pos == 7){
//Horizontal
if (a[2][0] == a[2][1] && a[2][0] == a[2][2]){
if(a[2][0] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//Vertical
if(a[0][0] == a[1][0] && a[0][0] == a[2][0]){
if(a[2][0] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//diagonal
if(a[2][0] == a[1][1] && a[2][0] == a[0][2]){
if(a[2][0] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}}
if(pos == 8){//Horizontal
if (a[2][0] == a[2][1] && a[2][0] == a[2][2]){
if(a[2][1] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//Vertical
if(a[0][1] == a[1][1] && a[0][1] == a[2][1]){
if(a[2][1] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;
}}}
if(pos == 9){
//Horizontal
if (a[2][0] == a[2][1] && a[2][0] == a[2][2]){
if(a[0][2] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;
}}
//Vertical
if(a[0][2] == a[1][2] && a[0][2] == a[2][2]){
if(a[2][2] == 1){
printf("Player 1 wins!\n");
counter++;}
else{
printf("Player 2 wins!\n");
counter++;}}
//diagonal
if(a[2][2] == a[1][1] && a[2][2] == a[0][0]){
if(a[0][2] == 1){
printf("Player 1 wins!\n");
counter++;}else{
printf("Player 2 wins!\n");
counter++;
}
}
}

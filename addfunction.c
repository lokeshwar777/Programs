#include<stdio.h>
int addition(int,int);	//declaration(prototype)8
void main()
{	
	int a,b,c;
	printf("Enter the value of a:");
	scanf("%d",&a);
	printf("Enter the value of b:");
	scanf("%d",&b);
	c=addition(a,b);	//call
	printf("The result is %d",c);
}
int addition(a,b)	//definition
{
	return a+b;
}

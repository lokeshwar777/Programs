#include<stdio.h>
int division(int,int);
void main()
{
	int a,b,c;
	printf("Enter the value of a:");
	scanf("%d",&a);
	printf("Enter the value of b:");
	scanf("%d",&b);
	c=division(a,b);	//call
	printf("The division of a and b is %d",c);
}
int division()
{
	return a/b;
}

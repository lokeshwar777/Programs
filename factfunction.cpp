#include<stdio.h>
int factorial(int);
int main()
{
	int a,b;
	printf("Enter a number:");
	scanf("%d",&a);
	b=factorial(a);
	printf("Factorial of the number is %d",b);
}
int factorial(int a)
{
	int i,b=1;
	for(i=1;i<=a;i++)
		b=b*i;
	return b;
}

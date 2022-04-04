#include<stdio.h>
#include<math.h>
main()
{	int a,b,c,d,k,n,x;
	printf("Enter a number");
	scanf("%d",&x);
	printf("The strong numbers from 1 to %d are \n",x);
	for(n=1;n<=x;n++)
		{	k=n;
			d=0;
			while(n>0)
				{	a=n%10;
					c=1;
					for(b=a;b>0;b--)
					{	c=c*b;
					}
				d=d+c;
				n=n/10;
				}
		if(k==d)
			{	printf("%d\n",k);
			}
		n=k;
		}
}		

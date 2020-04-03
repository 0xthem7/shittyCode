#include <stdio.h>
int main(){
	int a;
	printf("\033[34,41,1mEnter your age=");
	scanf("%d",&a);
	if(a>12&&a<20)
	printf("your teen");
	else if(a>20&&a<50)
	printf("your Adult");
	else if(a>=50)
	printf("your Old");
	else
	
		
	printf("your baby");
	return 0;}
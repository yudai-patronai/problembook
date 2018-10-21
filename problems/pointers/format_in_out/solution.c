#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *format, *a;
	format = malloc(21);
	a = calloc(1, 21);

	fgets(format, 20, stdin);
	scanf(format, a);
	fgets(format, 20, stdin);
	if (a[8]!='\0'){
		printf(format, a);
	}
	else if(a[4] != '\0')
	{	
		double tmp = *(double*)a;
		printf(format, tmp);
	}
	else{
		long tmp = *(long*)a;
		printf(format, tmp);	
	}

	free(a);
	free(format);
	return 0;
}
#include <stdio.h>
#include <stdlib.h>

void print_no_space(char* text);

int main()
{
	char * text = NULL;
	size_t i = 1;
	getline(&text, &i, stdin);
	print_no_space(text);
	return 0;
}

#define long NONETYPE_LONG
#define short NONETYPE_SHORT
#define int NONETYPE_INT
#define float NONETYPE_FLOAT
#define double NONETYPE_FLOAT
#define wchar NONETYPE_WCHAR


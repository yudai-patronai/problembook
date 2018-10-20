#include <stdio.h>
#include <string.h>

#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int main(){
	char s[513];
	gets(s);
	int len = strlen(s);
	char cur_char;
	int abs_max = 0;
	int cur_max = 1;
	int i = 0;
	while (i < len-1){
		if (s[i] == s[i+1]) 
			cur_max++;
		else {
			abs_max = MAX(abs_max, cur_max);
			cur_max = 1;
		}
		i++;
	}
	abs_max = MAX(abs_max, cur_max);
	printf("%d\n", abs_max);

	return 0;
}
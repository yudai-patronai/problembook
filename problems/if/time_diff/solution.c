#include <stdio.h>

int main() {
	int h1, m1, s1;
	int h2, m2, s2;
	scanf("%02d:%02d:%02d", &h1, &m1, &s1);
	scanf("%02d:%02d:%02d", &h2, &m2, &s2);
	int ss1, ss2;
	ss1 = s1 + m1*60 + h1*60*60;
	ss2 = s2 + m2*60 + h2*60*60;

	if (ss1 <= ss2)
		printf("%d", ss2 - ss1);
	else {
		int diff = 24*60*60 - ss1 + ss2;
		printf("%d", diff);
	}
	return 0;
}
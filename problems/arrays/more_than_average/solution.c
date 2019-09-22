#include <stdlib.h>
#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	
	int array[n];
	int sum = 0;
	
	for (int i = 0; i < n; ++i) {
		scanf("%d", &array[i]);
		sum += array[i];
	}
	
	float average = sum / (float) n;
	sum = 0;
	
	for (int i = 0; i < n; ++i) {
		if (array[i] > average) {
			sum += array[i];
		}		
	}  
	
	printf("%d\n", sum);
	return 0;
}

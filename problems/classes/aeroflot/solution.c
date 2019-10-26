#include <stdlib.h>
#include <stdio.h>

struct aeroflot {
	int departure;
	int destination;
	int points[3];
};

int main() {
	int n;
	int departure, destination, day;
	int sum = 0;
	scanf("%d", &n);
	
	struct aeroflot array[n];
	
	for (int i = 0; i < n; ++i) {
		scanf("%d %d %d %d %d", &array[i].departure, &array[i].destination, 
			&array[i].points[0], &array[i].points[1], &array[i].points[2]);
	}
	
	scanf("%d %d %d", &departure, &destination, &day);
	for (int i = 0; i < n; ++i) {
		if (array[i].departure == departure && array[i].destination == destination) {
			for (int j = 0; j < 3; ++j) {
				if (array[i].points[j] >= day) {
					++sum;
				}
			}
		}
	}
	
	printf("%d\n", sum);
}

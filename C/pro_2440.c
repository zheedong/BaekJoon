#include <stdio.h>
#pragma warning (disable:4996)

int main() {
	int row = 0;
	scanf("%d", &row);

	for (int i = row; i > 0; i--) {
		for (int j = 0; j < i; j++)
			printf("*");
		printf("\n");
	}

	return 0;
}
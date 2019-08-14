#include <stdio.h>
#pragma warning (disable:4996)

int main() {
	int row = 0;
	scanf("%d", &row);

	for (int i = row; i > 0; i--) {
		for (int p = row - i; p > 0; p--)
			printf(" ");
		for (int j = i; j > 0; j--)
			printf("*");
		printf("\n");
	}

	return 0;
}
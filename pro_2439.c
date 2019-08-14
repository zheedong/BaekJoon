#include <stdio.h>
#pragma warning (disable:4996)

int main() {
	int row = 0;
	scanf("%d", &row);

	for (int i = row; i > 0; i--) {
		for (int j = i - 1; j > 0; j--)
			printf(" ");
		for (int p = row - i + 1; p > 0; p--)
			printf("*");
		printf("\n");
	}

	return 0;
}
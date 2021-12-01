#include <stdio.h>
#pragma warning (disable:4996)

int main() {
	int row = 0;
	scanf("%d", &row);

	for (int i = 1; i <= row; i++) {
		for (int j = 1; j <= row - i; j++)
			printf(" ");
		for (int p = 1; p <= 2 * i - 1; p++)
			printf("*");
		printf("\n");
	}
	for (int i = row - 1; i >= 0; i--) {
		for (int j = 1; j <= row - i; j++)
			printf(" ");
		for (int p = 1; p <= 2 * i - 1; p++)
			printf("*");
		printf("\n");
	}
	return 0;
}
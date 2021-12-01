#include <stdio.h>
#pragma warning(disable:4996)

int main() {
	int n = 0;
	scanf("%d", &n);

	for (int i = 1; i <= 9; i++) {
		printf("%d * %d = %d\n", n, i, n*i);
	}

	return 0;
}
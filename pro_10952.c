#include <stdio.h>

int main() {
	int a = 1, b = 1, res = 0;

	while (a != 0 && b != 0) {
		scanf("%d %d", &a, &b);
		res = a + b;
		if (res == 0)
			break;
		printf("%d", res);
	}

	return 0;
}
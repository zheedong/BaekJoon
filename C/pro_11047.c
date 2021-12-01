#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

//Å½¿å ¾Ë°í¸®Áò

int main() {
	int n, sum = 0;
	int count = 0;
	unsigned int k = 0;
	int buffer[1000000] = { '0', };
	scanf("%d %d", &n, &k);

	for (int i = 0; i < n; i++) {
		scanf("%d", &buffer[i]);
	}
	
	while (sum != k) {
		for (int i = n - 1; i >= 0; i--) {
			if (sum + buffer[i] <= k) {
				sum += buffer[i];
				count++;
				break;
			}
		}
	}
	printf("%d\n", count);
	return 0;
}
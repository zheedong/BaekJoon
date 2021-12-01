#include <stdio.h>

int main() {
	int buffer[10];
	int i = 0;

	scanf_s("%d", &i);

	for (int count = 0; count < i; count++) {
		scanf_s("%d", &buffer[count]);
	}

	for (int j = i - 1; j > 0; j--) {
		for (int k = 0; k < i; k++) {
			if (buffer[k] > buffer[k + 1]) {
				int buf = 0;
				buf = buffer[k];
				buffer[k] = buffer[k + 1];
				buffer[k + 1] = buf;
			}
		}
	}

	printf("%d %d", buffer[0], buffer[i - 1]);
	
	return 0;
}
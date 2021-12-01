#include <stdio.h>
#pragma warning (disable : 4996)

int main() {
	int T = 0;
	int R = 0;
	char S[20] = { '\0', };

	scanf("%d", &T);

	for (int j = 0; j < T; j++) {
		scanf("%d %s", &R, S);
		for (int i = 0; S[i]; i++) {
			for (int k = 0; k < R; k++) {
				printf("%c", S[i]);
			}
		}
		printf("\n");
	}

	return 0;
}

#include <stdio.h>
#include <string.h>
#pragma warning(disable : 4996)

int main() {
	int count = 0;
	char buffer[100] = { '\0', };
	gets(buffer);

	char *ptr = strtok(buffer, " ");

	while (ptr != NULL) {
		count++;
		ptr = strtok(NULL, " ");
	}

	printf("%d", count);

	return 0;
}
#include <stdio.h>
#pragma warning (disable : 4996)

int main() {
	int output = 0;
	int counter = 0;
	char* inp_buf;
	int* int_buf;
	scanf("%d", &counter);
	inp_buf = (char*)malloc(sizeof(char) * (counter + 1));
	int_buf = (int*)malloc(sizeof(int) * counter);

	scanf("%s", inp_buf);
	for (int i = 0; i < counter; i++) {
		int_buf[i] = inp_buf[i] - '0';
		output += int_buf[i];
	}

	printf("%d\n", output);

	free(inp_buf);
	free(int_buf);
	return 0;
}

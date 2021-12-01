#include <stdio.h>
#include <stdbool.h>
#pragma warning (disable : 4996)

int main() {
	char inp_buf[101] = { '\0', };
	bool flag;

	scanf("%s", inp_buf);
	for (int alpa = 'a'; alpa <= 'z'; alpa++) {
		flag = false;
		for (int i = 0; inp_buf[i]; i++) {
			if (inp_buf[i] == alpa) {
				printf("%d ", i);
				flag = true;
				break;
			}
		}
			printf("-1 ");
		if(!flag)
	}

	return 0;
}

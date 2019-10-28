#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#pragma warning (disable : 4996)

int main() {
	char inp_buf[1000000] = { '\0', };
	int alpa_counter[26] = { 0, };
	bool flag = true;

	scanf("%s", inp_buf);
	//strupr(inp_buf);
	for (int j = 0; inp_buf[j]; j++) {
		if (inp_buf[j] >= 'a' && inp_buf[j] <= 'z') {
			inp_buf[j] += 'A' - 'a';
		}
	}

	for (int j = 0; inp_buf[j]; j++) {
		for (int i = 0; i < 26; i++) {
			if (inp_buf[j] == i + 'A') {
				alpa_counter[i]++;
				break;
			}
		}
	}

	int biggest_index = 0;
	for (int i = 1; i < 26; i++) {
		if (alpa_counter[i] > alpa_counter[biggest_index]) {
			biggest_index = i;
			flag = true;
		}
		else if (alpa_counter[i] == alpa_counter[biggest_index]) {
			biggest_index = i;
			flag = false;
		}
	}

	printf("%c", flag ? biggest_index + 'A' : '?');

	return 0;
}

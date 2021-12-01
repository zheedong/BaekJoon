#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#pragma warning (disable : 4996)

bool _Search(char ch, char* str) {
	for (int i = 0; str[i]; i++) {
		if (str[i] == ch)
			return true;
	}
	return false;
}

void _Save(char ch, char* str) {
	/*
	bool _Search(char ch, String str)
		Loop for all String
			if found, ret true
			else ret false
	*/

	int i = 0;
	for (; str[i]; i++);
	str[i] = ch;
}

int main() {
	int N = 0;
	int total_counter = 0;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		bool flag = true;
		char inp_arr[101] = { '\0', };
		char found_arr[101] = { '\0', };
		scanf("%s", inp_arr);
		/*
		Loop for all String
			if(_Search)
				if(str [i-1] != str[i+1])
					flag = false;
					break;
			else
				void _Save(char ch, String str);
		*/
		for (int j = 0; inp_arr[j]; j++) {
			if (_Search(inp_arr[j], found_arr)) {
				if (inp_arr[j - 1] != inp_arr[j]) {
					flag = false;
					break;
				}
			}
			else {
				_Save(inp_arr[j], found_arr);
			}
		}
		
		if (flag)
			total_counter++;
	}
	printf("%d", total_counter);
	return 0;
}

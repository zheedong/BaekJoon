#include <stdio.h>
#pragma warning (disable : 4996)

int main() {
	/*
	counter=0;
	Loop for every string
		if ch + 1 == NULL
			counter++;	
			break;
		if ch == c
			if ch + 1 == =
				counter++;	
				i+=2;	
			else if ch + 1 == -
		else if ch == d
			if ch + 1
		.
		.
		.
		else
			counter++;	
			i+=1;
	*/
	char Word[101] = { '\0', };
	int counter = 0;
	int i = 0;
	scanf("%s", Word);

	for (; Word[i]; i++) {
		if (Word[i + 1] == NULL) {
			counter++;
			continue;
		}

		if (Word[i] == 'c') {
			if (Word[i + 1] == '=') {
				counter++;
				i++;
				continue;
			}
			else if (Word[i + 1] == '-') {
				counter++;
				i++;
				continue;
			}
		} //c end

		if (Word[i] == 'd') {
			if (Word[i + 1] == '-') {
				counter++;
				i++;
				continue;
			}
			else if (Word[i + 2] == NULL) {
				counter++;
				continue;
			}
			else if (Word[i + 1] == 'z' && Word[i + 2] == '=') {
				counter++;
				i += 2;
				continue;
			}
		} //d end

		if (Word[i] == 'l' && Word[i+1] == 'j') {
			counter++;
			i++;
			continue;
		}//lj

		if (Word[i] == 'n' && Word[i + 1] == 'j') {
			counter++;
			i++;
			continue;
		}//nj

		if (Word[i] == 's' && Word[i + 1] == '=') {
			counter++;
			i++;
			continue;
		}//s=

		if (Word[i] == 'z' && Word[i + 1] == '=') {
			counter++;
			i++;
			continue;
		}//z=

		counter++;
	}

	printf("%d\n", counter);
	return 0;
}
